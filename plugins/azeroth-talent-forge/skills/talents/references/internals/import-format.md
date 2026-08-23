# Blizzard import/export format

The local codec decodes the Retail talent bitstream: serialization version, specialization ID, tree-hash field, then the spec's stored ascending node-ID order. Each selected slot records ranks and, for selection nodes, a choice marker and choice index.

A non-zero tree hash must match the bundled build. A zero tree hash is accepted under Blizzard's third-party policy, but cannot prove the client patch that produced it. Zero-only tail bits may be omitted. The decoder also preserves an accepted legacy missing first-choice marker on unchanged re-export; edits emit the current marker form.

Import proves only structural compatibility with this local graph. Validation additionally checks topology and the requested level's independent point pools. Export returns a Blizzard-compatible string and a Wowhead share URL without making a network request.
