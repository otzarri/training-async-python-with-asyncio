# Run with: python -W ignore 01-coroutine-objects-and-async-functions.py

import asyncio
import inspect


async def main():
    pass

print("- Type of `main` function:", type(main))
print("- Is `main` a coroutine function?", inspect.iscoroutinefunction(main))
print("- Get the return type of `main` function: ", type(main()))
print("- Display the contents of `main` function: ", dir(main()))
