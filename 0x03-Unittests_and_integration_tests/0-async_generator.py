#!/usr/bin/env python3
import asyncio
import random


async def async_generator():
    """
    Coroutine that generates 10 random numbers between 0 and 10 with a 1 second delay between each numbers.

    Yields:
        int: A random integer between 0 and 10.
    """
    for z in range(10):
        await asyncio.sleep(1)  # Wait for 1 second asynchronously
        yield random.randint(0, 10)  # Generate a random number between 0 and 10 and yield it to the caller
