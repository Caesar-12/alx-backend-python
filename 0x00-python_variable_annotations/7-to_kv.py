#!/usr/bin/env python3
"""Contains to_kv function"""
from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, (v * v))
