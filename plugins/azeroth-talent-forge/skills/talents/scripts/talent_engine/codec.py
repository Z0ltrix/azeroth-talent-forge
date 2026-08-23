"""Blizzard Retail talent-string codec (serialization version 2)."""

from __future__ import annotations

from .errors import TalentError
from .models import Selection, SnapshotIdentity, SpecGraph, TalentBuild


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


class BitReader:
    def __init__(self, text: str):
        if not text or any(char not in ALPHABET for char in text):
            raise TalentError("INVALID_IMPORT_STRING", "the string contains a character outside the Blizzard alphabet")
        self.values = [ALPHABET.index(char) for char in text]
        self.position = 0

    def read(self, width: int) -> int:
        value = 0
        for shift in range(width):
            index, offset = divmod(self.position, 6)
            if index >= len(self.values):
                raise TalentError("BODY_UNDERFLOW", "the import string ended before the node body was complete")
            value |= ((self.values[index] >> offset) & 1) << shift
            self.position += 1
        return value

    def remaining_nonzero(self) -> bool:
        while self.position < len(self.values) * 6:
            index, offset = divmod(self.position, 6)
            if (self.values[index] >> offset) & 1:
                return True
            self.position += 1
        return False


class BitWriter:
    def __init__(self):
        self.bits: list[int] = []

    def add(self, width: int, value: int) -> None:
        if value < 0 or value >= (1 << width):
            raise TalentError("RANK_OUT_OF_RANGE", f"value {value} does not fit in {width} bits")
        self.bits.extend((value >> shift) & 1 for shift in range(width))

    def finish(self) -> str:
        output: list[str] = []
        for offset in range(0, len(self.bits), 6):
            value = 0
            for bit_offset, bit in enumerate(self.bits[offset:offset + 6]):
                value |= bit << bit_offset
            output.append(ALPHABET[value])
        return "".join(output)


def decode_header(code: str) -> tuple[int, int, bytes | None]:
    reader = BitReader(code)
    version = reader.read(8)
    spec_id = reader.read(16)
    tree_hash = bytes(reader.read(8) for _ in range(16))
    return version, spec_id, None if tree_hash == bytes(16) else tree_hash


def decode_build(code: str, graph: SpecGraph, *, level: int = 80) -> TalentBuild:
    reader = BitReader(code)
    version = reader.read(8)
    spec_id = reader.read(16)
    tree_hash = bytes(reader.read(8) for _ in range(16))
    if version != graph.snapshot.serialization_version:
        raise TalentError("UNSUPPORTED_SERIALIZATION_VERSION", f"serialization version {version} is unsupported")
    if spec_id != graph.spec_id:
        raise TalentError("UNSUPPORTED_SPEC", f"string specialization {spec_id} does not match graph {graph.spec_id}")
    selections: list[Selection] = []
    for node in graph.nodes:
        purchased = reader.read(1) == 1
        if not purchased:
            continue
        selected = reader.read(1) == 1
        if not selected:
            selections.append(Selection(node.node_id, node.entry_id, 0, node.max_ranks))
            continue
        partial = reader.read(1) == 1
        ranks = reader.read(6) if partial else node.max_ranks
        is_choice = reader.read(1) == 1
        choice_index = reader.read(2) if is_choice else 0
        if ranks < 1 or ranks > node.max_ranks:
            raise TalentError("RANK_OUT_OF_RANGE", f"node {node.node_id} has rank {ranks}", node_id=node.node_id)
        if is_choice and choice_index >= max(node.choice_count, 1):
            raise TalentError("CHOICE_CONFLICT", f"node {node.node_id} has invalid choice {choice_index}", node_id=node.node_id)
        selections.append(Selection(node.node_id, node.entry_id, ranks, 0, choice_index))
    if reader.remaining_nonzero():
        raise TalentError("NONZERO_UNUSED_BITS", "unused import-string bits are non-zero")
    observed_hash = None if tree_hash == bytes(16) else tree_hash
    identity = SnapshotIdentity(graph.snapshot.game_build, graph.snapshot.locale, version, spec_id, graph.snapshot.asset_sha256, False)
    return TalentBuild(identity, graph.class_id, spec_id, level, None, observed_hash, tuple(selections))


def encode_build(build: TalentBuild, graph: SpecGraph) -> str:
    if build.spec_id != graph.spec_id:
        raise TalentError("UNSUPPORTED_SPEC", "build and graph specialization differ")
    selections = {selection.node_id: selection for selection in build.selections}
    writer = BitWriter()
    writer.add(8, graph.snapshot.serialization_version)
    writer.add(16, graph.spec_id)
    writer.add(128, 0)
    for node in graph.nodes:
        selection = selections.get(node.node_id)
        granted = bool(selection and selection.observed_granted_ranks > 0 and selection.purchased_ranks == 0)
        selected = bool(selection and selection.purchased_ranks > 0)
        writer.add(1, 1 if granted or selected else 0)
        if not (granted or selected):
            continue
        writer.add(1, 1 if selected else 0)
        if not selected:
            continue
        ranks = selection.purchased_ranks
        if ranks < 1 or ranks > node.max_ranks:
            raise TalentError("RANK_OUT_OF_RANGE", f"node {node.node_id} has rank {ranks}", node_id=node.node_id)
        partial = ranks != node.max_ranks
        writer.add(1, 1 if partial else 0)
        if partial:
            writer.add(6, ranks)
        writer.add(1, 1 if node.is_choice else 0)
        if node.is_choice:
            if selection.choice_index >= max(node.choice_count, 1):
                raise TalentError("CHOICE_CONFLICT", f"node {node.node_id} has invalid choice", node_id=node.node_id)
            writer.add(2, selection.choice_index)
    return writer.finish()
