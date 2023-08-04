#!/usr/bin/env python3
"""Contains function sum_list"""
#from typing import Sequence


def sum_list(input_list: list[float]) -> float:
    """Calculates the sum of floats in the given list"""
    sum: float = 0
    for num in input_list:
        sum += num

    return sum
