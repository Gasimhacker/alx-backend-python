#!/usr/bin/env python3
"""
A module that defines a function that
sums a list of numbers
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of float numbers"""
    ans: float = 0
    for num in input_list:
        ans += num
    return ans
