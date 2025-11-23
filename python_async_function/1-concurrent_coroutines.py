#!/usr/bin/env python3
"""Module that defines the wait_n coroutine."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run wait_random n times with the specified max_delay.
    Return a list of delays in ascending order,
    using concurrency behavior rather than sort().

    Args:
        n (int): number of tasks to run
        max_delay (int): maximum delay for wait_random

    Returns:
        List[float]: list of delays in ascending order
    """
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    for completed in asyncio.as_completed(tasks):
        delay = await completed
        delays.append(delay)

    return delays
