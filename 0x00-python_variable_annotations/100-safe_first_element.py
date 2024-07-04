#!/usr/bin/env python3
"""
A module that defines a function that
returns the first element of a sequence if possible
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a sequence if possible"""
    if lst:
        return lst[0]
    else:
        return None
