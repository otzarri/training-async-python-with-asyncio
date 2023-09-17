import asyncio


# Context manager. An object that implements both `__enter__()`
# and `__exit__()` methods is called a context manager.
class Connection:
    # Async enter. Returns awaitable.
    # Called when starting an `async with` block whereas
    # the `__aexit__()` method is called at the end. 
    async def __aenter__(self):
        print('Setting up a connection')
        # Simulate connection creation.
        await asyncio.sleep(1)
        # Return simulated connection.
        return {'driver': 'sqlite'}

    # Async exit. Returns awaitable.
    # Called when ending an `async with` block whereas
    # the `__aenter__()` method is called at the start.
    async def __aexit__(self, exc_type, exc, tb):
        # Remove simulated connection.
        await asyncio.sleep(1)
        print('Connection is closed')


async def main():
    async with Connection() as db:
        print(db, 'is ready')

asyncio.run(main())
