import asyncio

# Create a native coroutine using the "async" keyword when creating a function.
# Python coroutines are awaitables and therefore can be awaited from other coroutines:
async def main():
    print('hello...')
    # Passes function control back to the event loop
    await asyncio.sleep(2)
    print('...world')

# Runs the passed coroutine, taking care of managing the asyncio event loop,
# finalizing asynchronous generators, and closing the threadpool.
# Cannot be called when another asyncio event loop is running in the same thread.
asyncio.run(main())
