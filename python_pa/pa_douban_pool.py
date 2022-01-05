# -*- coding:utf-8 -*-

from concurrent import futures
import threading
import requests
from bs4 import BeautifulSoup
from multiprocessing import current_process
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'Referer': 'https://book.douban.com/'
}


def get_html(url):
    
    print("当前父进程：{}".format(current_process().pid))
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'lxml')
    title = soup.select('h1 span')[0].text
    print(title)


def get_link(url):

    print("当前父进程：{}".format(current_process().pid))
    html = requests.get(url, headers=headers)
    threadpools = ThreadPoolExecutor(max_workers=3)
    soup = BeautifulSoup(html.text, 'lxml')
    books_link = soup.select('.subject-item')

    for book in books_link:
        link = book.select('h2 a')[0]['href']
        threadpools.submit(get_html, link)


def main():

    urls = [
        'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4',
        'https://book.douban.com/tag/%E9%9A%8F%E7%AC%94',
        'https://book.douban.com/tag/%E6%95%A3%E6%96%87'
    ]

    with ProcessPoolExecutor(max_workers=3) as executor:
        future = [executor.submit(get_link, url) for url in urls]


if __name__ == '__main__':

    main()