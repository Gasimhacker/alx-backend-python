#!/usr/bin/env python3
"""
A module that defines a function that
return a function that multiply with multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiply with multiplier"""
    def multiply(arg: float) -> float:
        return arg * multiplier
    return multiply
