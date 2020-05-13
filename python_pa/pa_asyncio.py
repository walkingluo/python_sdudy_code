# -*- coding:utf-8 -*-

import time
'''
def job(t):
    print("Start job", t)
    time.sleep(t)
    print("Job", t, "takes", t, 's')

def main():
    [job(t) for t in range(1,3)]

t1 = time.time()
main()
print("No async total time: ", time.time()-t1)
'''
import asyncio
'''
async def job(t):
    print("Start job", t)
    await asyncio.sleep(t)
    print("Job", t, "takes", t, 's')

async def main(loop):
    tasks = [
    loop.create_task(job(t)) for t in range(1,3)
    ]
    await asyncio.wait(tasks)
'''
import requests
import aiohttp

URL = 'https://morvanzhou.github.io/'

async def job(session):
    response = await session.get(URL)       # 等待并切换
    return str(response.url)

async def main(loop):
    async with aiohttp.ClientSession() as session:
        tasks = [loop.create_task(job(session)) for _ in range(2)]
        finished, unfinished = await asyncio.wait(tasks)
        all_results = [r.result() for r in finished]    # 获取所有结果
        print(all_results)

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
print("Async total time:", time.time()-t1)