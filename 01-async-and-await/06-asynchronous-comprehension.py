import asyncio


async def download(urls):
    for url in urls:
        await asyncio.sleep(1)
        response = {'status': 200, 'data': f'content of {url}'}
        if url == 'bing.com':
            response['status'] = 500
        yield response


async def handle(err_response):
    print('logging error response for', err_response)


async def main():
    urls = [
        'google.com',
        'bing.com',
        'duckduckgo.com',
    ]

    # List comprehension. Comprehensions in Python provide us
    # with a short and concise way to construct new sequences.
    errors = [r async for r in download(urls) if r['status'] != 200]
    print(errors)

    # Async list comprehension.
    [await handle(e) for e in errors]


asyncio.run(main())
