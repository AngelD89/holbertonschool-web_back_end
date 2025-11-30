#!/usr/bin/env python3
"""0-async_generator.py
Async generator that yields 10 random integers between 0 and 10,
waiting 1 second between each yield.
"""
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[int, None]:
    """Asynchronous generator that yields 10 random integers (0..10)."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
