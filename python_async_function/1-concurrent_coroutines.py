#!/usr/bin/env python3
"""Asynchronous wait_n coroutine module."""

import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times and returns list of delays in ascending order."""
    wait_random = __import__('0-basic_async_syntax').wait_random
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
