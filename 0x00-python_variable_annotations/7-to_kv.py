#!/usr/bin/env python3
"""
A module that defines a function that
returns a tuple of key and value
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of a string and a float"""
    return (k, v ** 2)
