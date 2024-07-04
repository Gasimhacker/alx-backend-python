#!/usr/bin/env python3
"""
A module that defines a function that
sums a list of floats and integers
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a mixed list of floats and integers"""
    ans: float = 0
    for num in mxd_lst:
        ans += num
    return ans
