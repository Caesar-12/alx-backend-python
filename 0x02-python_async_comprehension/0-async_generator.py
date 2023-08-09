#!/usr/bin/env python3
"""Contains async_generator coroutine"""
import asyncio
import random


async def async_generator() -> None:
    """Runs asynchronouslt 10 times waitin 1 second each time"""
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
