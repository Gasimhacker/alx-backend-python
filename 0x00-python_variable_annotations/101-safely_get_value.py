#!/usr/bin/env python3
"""
A module that defines a function that
returns a value from a dictionary safely
"""
from typing import Mapping, Union, Any, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Return a value from a dictionary safely"""
    if key in dct:
        return dct[key]
    else:
        return default
