#!/usr/bin/env python3
"""Defines a type-annotated make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Accepts a float and return a function that multiplies the float"""
    return lambda x: x * multiplier
