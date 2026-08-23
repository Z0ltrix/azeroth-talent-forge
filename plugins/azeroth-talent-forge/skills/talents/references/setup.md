---
feature: setup
---

# Local setup

The `talents` runtime uses Python 3.10–3.14 and the pinned embedded graph
database package `ladybug==0.19.1`. Ladybug is not a separate server: the
repository already bundles the read-only `talents.lbdb` asset. Create one
local virtual environment at the repository root and use its interpreter for
every talent command.

## Windows

Use an installed Python 3.10–3.14 explicitly if the system `python` command
points to an older interpreter:

```powershell
cd C:\path\to\azeroth-talent-forge
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r plugins\azeroth-talent-forge\requirements-talents.txt
```

If `py -3.12` is unavailable, install a supported 64-bit Python first. Do not
create the environment with Python 3.8 or a 32-bit interpreter.

Verify the dependency and bundled graph:

```powershell
\.venv\Scripts\python.exe -c "import sys, ladybug; print(sys.executable); print(sys.version); print(ladybug.__version__)"
\.venv\Scripts\python.exe plugins\azeroth-talent-forge\skills\talents\scripts\talents.py assets info
```

## macOS/Linux

```bash
cd /path/to/azeroth-talent-forge
python3.12 -m venv .venv
.venv/bin/python -m pip install -r plugins/azeroth-talent-forge/requirements-talents.txt
.venv/bin/python -c 'import sys, ladybug; print(sys.executable); print(sys.version); print(ladybug.__version__)'
.venv/bin/python plugins/azeroth-talent-forge/skills/talents/scripts/talents.py assets info
```

## Runtime and network boundary

The `pip install` step may need network access once. After the dependency and
assets are present, import, validation, comparison, modification, generation,
preset lookup, and export run locally without network access. Runtime opens
`talents.lbdb` read-only. It never downloads Ladybug, refreshes assets, fetches
guide URLs, uploads exports, or starts a database service.

If installation must happen in a network-isolated environment, provide a
compatible cached/wheel copy of `ladybug==0.19.1` and install it into `.venv`
with the same interpreter. Do not replace the pinned version with an arbitrary
Ladybug release; the asset manifest requires engine version `0.19.1`.

Run the talent tests with the same interpreter:

```powershell
.venv\Scripts\python.exe -m unittest discover -s plugins\azeroth-talent-forge\skills\talents\tests
```
