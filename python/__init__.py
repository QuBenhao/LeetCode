# Bootstrap: ensure project root is on sys.path for direct script execution
import sys
from pathlib import Path

_root = Path(__file__).resolve().parent.parent
_root_str = str(_root)
if _root_str not in sys.path:
    sys.path.insert(0, _root_str)