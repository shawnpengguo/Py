import aiohttp
import asyncio

async def spider(num):
    print('start: ', num)
    async with  aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            html = await response.text()
            print("Body:", html[:15], "...")


async def main():
     await spider(1)

if __name__ == '__main__':
    asyncio.run(main())