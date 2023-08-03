#!/usr/bin/env python3
"""Contains function sum_list"""


def sum_mixed_list(mxd_list: list[float, int]) -> float:
    """Calculates the sum of floats in the given list"""
    sum: float = 0
    for num in mxd_list:
        sum += num

    return sum
