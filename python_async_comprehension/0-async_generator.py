#!/usr/bin/env python3
"""
Async generator
"""

import asyncio
import rndom
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    """Yield a random number between 0 and 10, 10 times, with 1-second pauses."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
