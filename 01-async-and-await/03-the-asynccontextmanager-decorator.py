import asyncio
from contextlib import asynccontextmanager


# This function is a decorator that can be used to define a factory function
# for async with statement asynchronous context managers, without needing to
# create a class or separate __aenter__() and __aexit__() methods. It must be
# applied to an asynchronous generator function.
@asynccontextmanager
async def connection():
    print('Setting up connection')
    await asyncio.sleep(1)
    yield {'driver': 'sqlite'}
    await asyncio.sleep(1)
    print('Shutting down')


async def main():
    async with connection() as db:
        print(db, 'is ready')

asyncio.run(main())
