"""Immutable domain values shared by codec, graph, validator, and operations."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SnapshotIdentity:
    game_build: str
    locale: str
    serialization_version: int
    spec_id: int
    asset_sha256: str
    source_patch_verified: bool


@dataclass(frozen=True)
class Selection:
    node_id: int
    entry_id: int
    purchased_ranks: int
    observed_granted_ranks: int = 0
    choice_index: int = 0


@dataclass(frozen=True)
class TalentBuild:
    snapshot: SnapshotIdentity
    class_id: int
    spec_id: int
    level: int
    hero_subtree_id: int | None
    observed_tree_hash: bytes | None
    selections: tuple[Selection, ...]


@dataclass(frozen=True)
class BuildRequest:
    spec_id: int
    level: int
    hero_subtree_id: int | None
    required_entry_ids: frozenset[int]
    forbidden_entry_ids: frozenset[int]
    preferred_entry_weights: tuple[tuple[int, int], ...]


@dataclass(frozen=True)
class CodecNode:
    node_id: int
    entry_id: int
    max_ranks: int
    is_choice: bool = False
    is_granted: bool = False
    choice_count: int = 0
    visible: bool = True


@dataclass(frozen=True)
class SpecGraph:
    snapshot: SnapshotIdentity
    class_id: int
    spec_id: int
    nodes: tuple[CodecNode, ...]
    names: tuple[tuple[int, str], ...]
    descriptions: tuple[tuple[int, str, str], ...]
    required_edges: tuple[tuple[int, int], ...] = ()
    sufficient_edges: tuple[tuple[int, int], ...] = ()
    exclusions: tuple[tuple[int, int], ...] = ()
    budgets: tuple[tuple[int, int], ...] = ()
    grants: tuple[tuple[int, int], ...] = ()

    @property
    def node_by_id(self) -> dict[int, CodecNode]:
        return {node.node_id: node for node in self.nodes}

    @property
    def entry_by_id(self) -> dict[int, CodecNode]:
        return {node.entry_id: node for node in self.nodes}

    @property
    def name_by_entry(self) -> dict[int, str]:
        return dict(self.names)


@dataclass(frozen=True)
class Violation:
    code: str
    message: str
    node_id: int | None = None
    entry_id: int | None = None


@dataclass(frozen=True)
class ValidationResult:
    valid: bool
    violations: tuple[Violation, ...]


@dataclass(frozen=True)
class BuildDiff:
    kind: str
    node_id: int | None
    entry_id: int | None
    before: int | None
    after: int | None
