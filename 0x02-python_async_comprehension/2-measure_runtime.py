#!/usr/bin/env python3
"""
This module defines a coroutine that will
that will execute async_comprehension four times
in parallel using asyncio.gather
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Masure the execution time of 4 coroutines running concurrently"""
    start = time.perf_counter()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    elapsed = time.perf_counter() - start
    return elapsed
