from typing import *

try:
    from typing import Self
except ImportError:
    Self = Any

Cell = Tuple[int, int]
