import requests,httpx,aiohttp
import time
import asyncio


# request 同步 httpx同步和异步 aiohttp异步
# 103.19101309776306 request / request session 38.80703377723694
# 55.66955900192261 httpx / httpx session 46.1419198513031 / http async 3.9420650005340576
# 3.46130108833313  aiohttp




url = "https://docs.aiohttp.org/en/stable/"
headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

def request_test():
    start_time = time.time()
    session = requests.session()
    session.headers.update(headers)
    for i in range(100):
        html = session.get(url)
        print(html.status_code)
    end_time = time.time()
    print('request speed time: ', end_time - start_time)

def httpx_test():
    httpx_start_time = time.time()
    # session = httpx.Client()
    # session.headers.update(headers)
    for i in range(100):
        html = httpx.get(url)
        print(html.status_code)
    httpx_end_time = time.time()
    print('httpx speed time: ', httpx_end_time - httpx_start_time)

async def async_cl(num, cl):
    html = await cl.get(url)
    # print('httpx async start: {} {}'.format(num, html.status_code)) httpx
    print('httpx async start: {} {}'.format(num, html.status))

async def httpx_async_test():
    httpx_async_start_time = time.time()
    async with httpx.AsyncClient(headers=headers) as client:
        httpx_async_list = []
        for i in range(100):
            httpx_async_list.append(asyncio.create_task(async_cl(i, client)))
        await asyncio.gather(*httpx_async_list)

    httpx_async_end_time = time.time()
    print('httpx_async_speed_time: ', httpx_async_end_time-httpx_async_start_time)

async def aiohttp_async_test():
    aiohttp_async_start_time = time.time()
    async with aiohttp.ClientSession(headers=headers) as client:
        httpx_async_list = []
        for i in range(1000 ):
            httpx_async_list.append(asyncio.create_task(async_cl(i, client)))
        await asyncio.gather(*httpx_async_list)

    aiohttp_async_end_time = time.time()
    print('httpx_async_speed_time: ', aiohttp_async_end_time-aiohttp_async_start_time)

if __name__ == '__main__':
    # request_test()
    # httpx_test()
    asyncio.run(aiohttp_async_test())
