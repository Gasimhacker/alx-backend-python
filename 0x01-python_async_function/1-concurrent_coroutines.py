#!/usr/bin/env python3
"""A module that make calls an async function"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Call an async function n times"""
    res = await asyncio.gather(
            *list(map(lambda _: wait_random(max_delay), range(n))))
    return sorted(res)
