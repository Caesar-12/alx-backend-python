#!/usr/bin env python3
"""Contains make_multiplier function"""
from typing import Callable


def multiply(num: float, mult: float=0.00) -> float:
    """multiplies a number by num"""
    return (num * mult)

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return multiply(multiplier)