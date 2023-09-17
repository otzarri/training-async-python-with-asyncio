import asyncio


# Async generator. A generator is a function that returns an iterator that
# produces a sequence of values when iterated over. Uses `yield` instead of `return`.
async def download(urls):
    for url in urls:
        await asyncio.sleep(1)
        response = {'status': 200, 'data': f'content of {url}'}
        yield response


async def main():
    urls = [
        'google.com',
        'bing.com',
        'duckduckgo.com',
    ]

    # Iterate the async generator.
    async for value in download(urls):
        print(value)

asyncio.run(main())
