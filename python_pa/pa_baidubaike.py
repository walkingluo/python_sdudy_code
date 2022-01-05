# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


base_url = "https://baike.baidu.com"
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

with open("./python_pa/baike.txt", 'w') as f:
    for i in range(10):

        url = base_url + his[-1]
        try:
            html = urlopen(url).read()
            soup = BeautifulSoup(html, features='lxml')
            name_url = str(i) + soup.find('h1').get_text() + '  url:' + his[-1] + "\n"
            print(name_url)
            f.writelines(name_url)
            sub_urls = soup.find_all("a", {"target":"_blank", "href":re.compile(r'/item/(%.{2})+/\d+$')})
        except:
            i -= 1

        if len(sub_urls) != 0:
            his.append(random.sample(sub_urls, 1)[0]['href'])
        else:
            his.pop()