"""Public CLI facade: parser plus dispatch."""
from .parser import build_parser
from .dispatch import main
__all__ = ["build_parser", "main"]
