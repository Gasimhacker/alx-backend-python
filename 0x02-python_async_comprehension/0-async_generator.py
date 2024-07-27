#!/usr/bin/env python3
"""This module defines an async generator"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """An async generator that returns a random number from 1-10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
