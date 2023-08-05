#!/usr/bin/env python3
"""Contains make_multiplier function"""
from typing import Callable
import sys


def multiply(mult: float) -> float:
    """multiplies a number by num"""
    return (mult * sys.argv[0])


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function"""
    sys.argv[0] = multiplier
    return multiply
