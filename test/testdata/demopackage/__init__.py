"""A test package"""


import demopackage2

from . import _child_e, child_b
from ._child_d import Test
from .child_b import B
from .child_c import C

__all__ = [
    "Test",
    "B",
    "C",
    "child_b",
    "child_c",
    "demopackage2",
    "_child_e",
]
