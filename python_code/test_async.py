# -*- coding:utf-8 -*-

import asyncio

async def hello(i):

    print("hello ", i)
    await asyncio.sleep(3)
    print("world ", i)


def main():

    tasks = []
    for i in range(4):
        tasks.append(hello(i))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':

    main()