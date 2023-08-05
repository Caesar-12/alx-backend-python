#!/usr/bin env python3
"""Contains make_multiplier function"""
from typing import Callable


hold: float = 1.00
def multiply(mult: float = 0.00) -> float:
    """multiplies a number by num"""
    return (mult * hold)

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function"""
    hold = multiplier
    return multiply()

