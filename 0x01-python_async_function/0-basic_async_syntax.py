#!/usr/bin/env python3
"""A module that make an async function"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay number"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
