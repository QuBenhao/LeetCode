"""Path bootstrap for scripts that need project root on sys.path.

Usage (at top of any script under python/scripts/ or python/dev/):
    from python._path import setup; setup()

This ensures the project root is importable without relying on PYTHONPATH.
"""

import sys
from pathlib import Path


def setup():
    """Insert project root at the front of sys.path (idempotent)."""
    # python/_path.py → python/ → project root
    root = Path(__file__).resolve().parents[1]
    root_str = str(root)
    if root_str not in sys.path:
        sys.path.insert(0, root_str)
