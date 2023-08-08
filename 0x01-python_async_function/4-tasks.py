#!/usr/bin/env python3
"""Contains Async routine function"""
import asyncio


async def task_wait_n(n, max_delay):
    """Utilizes the wait_random function"""
    task_wait_random = __import__('3-tasks').task_wait_random

    wait_list = []
    for i in range(n):
        wait = task_wait_random(max_delay)
        wait_time = await wait
        # print(type(wait_time))
        wait_list.append(wait_time)

    return wait_list
