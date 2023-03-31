#!/usr/bin/env python3
"""Defines annotated sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Accepts a list of floats and returns their sum as loat"""
    a: float = 0.0
    for i in input_list:
        a += i
    return a
