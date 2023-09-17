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
    # Create a task object and include the coroutine.
    task = asyncio.create_task(stopwatch())
    # Define callback function to run when the task is done.
    task.add_done_callback(callb)
    # A future is an object that returns a value later in the futurebut not now.
    # Typically, a future object is the result of an asynchronous operation.
    # The line below checks if the task is an instance of Future.
    print(asyncio.isfuture(task))

    await task

asyncio.run(main())
