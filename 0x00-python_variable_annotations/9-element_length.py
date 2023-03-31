#!/usr/bin/env python3
"""Defines a duck typed function"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Accepts a sequence and returns a list of
    tuples of sequence and int"""
    return [(i, len(i)) for i in lst]
