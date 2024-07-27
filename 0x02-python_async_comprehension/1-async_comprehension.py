#!/usr/bin/env python3
"""
This module defines a coroutine that will
collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """An async generator that returns a random number from 1-10"""
    return [i async for i in async_generator()]
