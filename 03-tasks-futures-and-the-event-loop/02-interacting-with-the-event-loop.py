import asyncio


# Create the coroutine.
async def stopwatch():
    count = 0
    while count < 1:
        await asyncio.sleep(1)
        count += 1
        print(count)


# Callback function.
def callb(task):
    print('task is done', task)


async def main():
    # Event loop is not only a mechanism in Python. Its represented by an object
    # which is accesible to us inside the context of a coroutine.
    # The line below prints information about the event loop.
    print(asyncio.get_running_loop())
    # Create a task object and include the coroutine.
    task = asyncio.create_task(stopwatch())
    # Define callback function to run when the task is done.
    task.add_done_callback(callb)

    await task

asyncio.run(main())
