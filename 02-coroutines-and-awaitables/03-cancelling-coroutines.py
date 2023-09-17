import asyncio

# Async generator function to print incremental numbers uninterruptedly.
async def stopwatch():
    count = 0
    while True:
        await asyncio.sleep(1)
        count += 1
        print(count)


async def main():
    # Create the task.
    task = asyncio.create_task(stopwatch())
    # Freeze the main coroutine for 3 seconds.
    await asyncio.sleep(3)
    # Cancel the task and the coroutine inside.
    task.cancel()


asyncio.run(main())
