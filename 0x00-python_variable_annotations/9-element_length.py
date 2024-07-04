#!/usr/bin/env python3
"""
A module that defines a function that
returns a sequence along with its length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a sequence along with its length"""
    return [(i, len(i)) for i in lst]
