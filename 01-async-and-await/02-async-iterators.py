import asyncio
import random


# Object with iterable property
class EggBoiler:
    def __init__(self, amount):
        # Defines an iterable property.
        self.eggs = iter(range(1, amount + 1))

    # Async iterable. Returns an object that implements `__anext__` special method.
    def __aiter__(self):
        return self

    # Async next. Returns an awaitable object.
    async def __anext__(self):
        try:
            # Get the next egg using the `next` function.
            egg = next(self.eggs)
        # This exception is automatically raised after iterable is exhausted.
        except StopIteration:
            # Indicate that we are done iterating
            raise StopAsyncIteration
        return self.boil(egg)

    async def boil(self, egg):
        # Boiling takes random times to show the async behaviour.
        await asyncio.sleep(random.randint(2, 5))
        print(f'Egg #{egg} is boiling')


async def main():
    eggs = []
    # Asynchronous for loop
    async for egg in EggBoiler(4):
        eggs.append(egg)
    print('We wait for the eggs to boil...')
    # Pass the contents of `eggs` list as positional arguments.
    await asyncio.gather(*eggs)

asyncio.run(main())
