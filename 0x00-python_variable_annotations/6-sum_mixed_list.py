#!/usr/bin/env python3
"""Contains function sum_list"""
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Calculates the sum of floats in the given list"""
    sum: float = 0.00
    for num in mxd_list:
        sum += num

    return sum
