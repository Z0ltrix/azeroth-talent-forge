#!/usr/bin/env python3
"""Direct executable compatibility entrypoint for Warcraft Logs."""

from pathlib import Path
import sys

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from warcraftlogs_core.models import *  # noqa: F401,F403
from warcraftlogs_core.credentials import *  # noqa: F401,F403
from warcraftlogs_core.transport import *  # noqa: F401,F403
from warcraftlogs_core.metadata import *  # noqa: F401,F403
from warcraftlogs_core.reports import *  # noqa: F401,F403
from warcraftlogs_core.discovery import *  # noqa: F401,F403
from warcraftlogs_core.parser import build_parser
from warcraftlogs_core import dispatch as _dispatch
from warcraftlogs_core import models as _models
from warcraftlogs_core import credentials as _credentials
from warcraftlogs_core import transport as _transport
from warcraftlogs_core import metadata as _metadata
from warcraftlogs_core import reports as _reports
from warcraftlogs_core import discovery as _discovery


def main(argv=None):
    # Preserve the historical patchable module-level test surface while the
    # implementation remains split across focused service modules.
    for name in dir(_dispatch):
        if name not in ("main",) and not name.startswith("__") and name in globals():
            setattr(_dispatch, name, globals()[name])
    return _dispatch.main(argv)


def __getattr__(name):
    for module in (_models, _credentials, _transport, _metadata, _reports, _discovery, _dispatch):
        if hasattr(module, name):
            return getattr(module, name)
    raise AttributeError(name)


if __name__ == "__main__":
    raise SystemExit(main())
