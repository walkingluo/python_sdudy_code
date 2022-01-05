# -*- conding:utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'Referer': 'https://www.kuaidaili.com/free/'
}
'''
proxies = {
    'http': 'http://220.135.165.38:8080',
    'https': 'http://220.135.165.38:8080'
}
'''
def write_json(proxies):
    
    with open('./python_pa/proxy.json', 'w', encoding='utf-8') as f:
        json.dump(proxies, f)

def read_json():

    with open('./python_pa/proxy.json', 'r') as f:
        proxies = json.load(f)
        print(proxies)


def test_proxy(proxies):

    url = 'http://www.baidu.com'
    try:
        html = requests.get(url, proxies=proxies, timeout=3)
        print("这个代理OK! {}".format(proxies))
        write_json(proxies)
    except:
        print("这个代理不行！{}".format(proxies))


def kuai_dai_li():

    for i in range(1, 5):

        url = "https://www.kuaidaili.com/free/inha/{}/".format(i)
        html = requests.get(url, headers=headers)

        soup = BeautifulSoup(html.text, 'lxml')
        contents = soup.select('tbody tr')
        for c in contents:
            ip = c.select('td')[0].text
            port = c.select('td')[1].text
            print(ip, port)
            ip_addr = 'http://{}:{}'.format(ip, port)

            ip_proxy = {
                'http': ip_addr,
                'https': ip_addr
            }
            test_proxy(ip_proxy)


if __name__ == '__main__':

    kuai_dai_li()
    # test_proxy(proxies)
    # write_json(proxies)
    # read_json()