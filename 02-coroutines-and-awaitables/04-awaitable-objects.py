import asyncio


# An awaitable class must implement the `await` magic method.
class Stopwatch:
    async def __await__(self):
        yield


async def main():
    # `Await` only works with awaitables.
    await Stopwatch()


asyncio.run(main())
