#!/usr/bin/env python3
"""Type-annotated make_multiplier function module."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
