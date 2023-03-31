#!/usr/bin/env python3
"""Defines a type annotated to_kv"""
from typing import Union, Tuple
from math import sqrt


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Accepts a string and a float/int and return tuple of a
    string and a float"""
    x = v ** 2
#    x = float(x)
    return (k, x)
