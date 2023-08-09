#!/usr/bin/env python3
"""Contains measure_runtime coroutine"""
import asyncio
import time


async def measure_runtime() -> float:
    """Returns the time takem to run async_comprehension"""
    comp = __import__('1-async_comprehension').async_comprehension
    start_time = time.time()
    await asyncio.gather(
        comp(),
        comp(),
        comp(),
        comp()
    )
    end_time = time.time()
    time_taken = end_time - start_time

    return time_taken
