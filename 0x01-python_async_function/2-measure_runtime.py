#!/usr/bin/env python3
"""Contains a measure_time function"""
import time
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """Calculates elapsed time fir wait_n function"""
    wait_n = __import__('1-concurrent_coroutines').wait_n
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    time_taken = end_time - start_time

    return time_taken
