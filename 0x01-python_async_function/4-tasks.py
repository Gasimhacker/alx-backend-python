#!/usr/bin/env python3
"""A module that make calls an async function"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Call an async function n times"""
    res = await asyncio.gather(
            *list(map(lambda _: task_wait_random(max_delay), range(n))))
    return sorted(res)
