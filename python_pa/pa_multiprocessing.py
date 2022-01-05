# -*- conding:utf-8 -*-
import multiprocessing as mp
import time
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import re

base_url = 'https://morvanzhou.github.io/'

def crawl(url):
    response = urlopen(url)
    # time.sleep(0.1)             # slightly delay for downloading
    return response.read().decode()


def parse(html):
    soup      = BeautifulSoup(html, 'lxml')
    urls      = soup.find_all('a', {"href": re.compile('^/.+?/$')})
    title     = soup.find('h1').get_text().strip()
    page_urls = set([urljoin(base_url, url['href']) for url in urls])   # 去重
    url       = soup.find('meta', {'property': "og:url"})['content']
    return title, page_urls, url

if __name__ == '__main__':
    unseen = set([base_url,])
    seen   = set()

    restricted_crawl = True

    mp.freeze_support()
    pool = mp.Pool(8)
    while len(unseen) != 0:                # still get some url to visit
        if restricted_crawl and len(seen) >= 20:
            break
        #htmls = [crawl(url) for url in unseen]
        crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
        htmls      = [j.get() for j in crawl_jobs]
        #results   = [parse(html) for html in htmls]
        parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
        results    = [j.get() for j in parse_jobs]

        seen.update(unseen)         # seen the crawled
        unseen.clear()              # nothing unseen

        for title, page_urls, url in results:
            unseen.update(page_urls - seen)     # get new url to crawl
            print(title)