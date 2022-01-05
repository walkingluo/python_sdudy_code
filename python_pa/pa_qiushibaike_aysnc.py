# -*- coding:utf-8 -*-

import asyncio
from asyncio import windows_events
from os import close
from types import TracebackType
import aiohttp
from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}

def crawl(i):

    url = 'https://www.qiushibaike.com/text/page/{}/'.format(i)
    print("--正在爬取第{}页--".format(i))
    page = requests.get(url, headers=headers).text
    '''
    # 异步请求
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as html:
            print(html.status)
            page = await html.text()
            print('get page: ', i)
    '''
    soup = BeautifulSoup(page, 'lxml')
    author_names = soup.select('.article.block.untagged.mb15 .author.clearfix h2')
    for author in author_names:
        print(author.text.strip())


async def main():

    loop = asyncio.get_event_loop()
    '''
    tasks = [crawl(i) for i in range(1, 5)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    '''
    tasks = []
    with ThreadPoolExecutor(max_workers=3) as t:
        for i in range(1, 5):
            tasks.append(loop.run_in_executor(
                t,
                crawl,
                i
            ))


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()