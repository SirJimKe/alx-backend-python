#!/usr/bin/env python3
"""Concurrent coroutines"""


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    Spawns wait_random n times
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
