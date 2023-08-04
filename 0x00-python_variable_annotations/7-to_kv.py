#!/usr/bin/env python3
"""Contains to_kv function"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with passed string and square of int
    passed
    """
    return (k, (v * v))
