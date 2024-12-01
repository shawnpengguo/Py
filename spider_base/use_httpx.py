import httpx
import asyncio

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

# html = httpx.get("https://www.python-httpx.org/", headers=headers)
#
# print(html.text)


# client = httpx.Client(http2=True, headers=headers)
# html = client.get(url="https://www.python-httpx.org/")
# print(html.text)

# async

async def spider(num):
    print('start: ', num)
    client = httpx.AsyncClient(headers=headers, http2=True)
    html = await client.get("https://www.python-httpx.org/")
    print(html)
    await client.aclose()

async def main():
    await asyncio.gather(*[spider(1), spider(2), spider(3)])


if __name__ == '__main__':
     asyncio.run(main())