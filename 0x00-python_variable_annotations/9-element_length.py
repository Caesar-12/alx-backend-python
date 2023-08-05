#!/usr/bin/python3
"""Contains annotated element_lengthfunction"""
from typing import Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns the elgth of objects in lists"""
    return [(i, len(i)) for i in lst]
