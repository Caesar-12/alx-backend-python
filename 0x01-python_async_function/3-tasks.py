#!/usr/bin/env python3
"""Contains task_wait_random function"""
import asyncio


def task_wait_random(max_delay):
    """Returns an asyncio.Task"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    wait_task = asyncio.create_task(wait_random(max_delay))

    return wait_task
