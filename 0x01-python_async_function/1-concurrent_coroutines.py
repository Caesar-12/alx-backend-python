#!/usr/bin/env python3
"""Contains Async routine function"""
import asyncio


async def wait_n(n, max_delay):
    """Utilizes the wait_random function"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    wait_list = []
    for i in range(n):
        wait = asyncio.create_task(wait_random(max_delay))
        wait_time = await wait
        # print(type(wait_time))
        wait_list.append(wait_time)

    return wait_list
