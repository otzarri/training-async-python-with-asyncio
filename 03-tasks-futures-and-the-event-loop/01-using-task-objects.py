import asyncio


# Create the coroutine.
async def stopwatch():
    count = 0
    while count < 4:
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

    # Run the task.
    await task


asyncio.run(main())
