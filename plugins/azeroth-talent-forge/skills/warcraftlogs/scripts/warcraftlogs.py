#!/usr/bin/env python3
"""Direct executable compatibility entrypoint for Warcraft Logs."""

from pathlib import Path
import sys

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from warcraftlogs_core import _legacy as _impl

# Keep the historical module-level testing/integration surface while the
# implementation lives behind the package boundary.  Synchronising names
# before dispatch also preserves callers that patch transport/client symbols.
for _name in dir(_impl):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_impl, _name)


def __getattr__(name):
    return getattr(_impl, name)


def main(argv=None):
    for _name in dir(_impl):
        if _name not in {"main", "_impl"} and not _name.startswith("__") and _name in globals():
            setattr(_impl, _name, globals()[_name])
    return _impl.main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
