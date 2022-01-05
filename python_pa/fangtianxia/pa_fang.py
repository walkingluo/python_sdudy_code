# -*- coding:utf-8 -*-

import threading
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import quote
from db import Fang, sess
from concurrent.futures import ThreadPoolExecutor

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'cookie': 'city=gz; global_cookie=8to28852tyw7c43x41v3dju5k17kknmgsrb; __utma=147393320.56836883.1612247398.1612247398.1612247398.1; __utmc=147393320; __utmz=147393320.1612247398.1.1.utmcsr=gz.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; showCity=b"\xc3\xa5\xc2\xb9\xc2\xbf\xc3\xa5\xc2\xb7\xc5\xbe"; newhouse_user_guid=4F4C4ED9-FA27-8357-0B96-C1C2E5E35D4D; newhouse_chat_guid=C50A1848-961D-01A4-27CF-223182592717; csrfToken=Cgp18ZTDEQI9yPMG8L848OV8; lastscanpage=0; g_sourcepage=esf_fy%5Elb_pc; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; unique_cookie=U_8to28852tyw7c43x41v3dju5k17kknmgsrb*18; __utmb=147393320.57.10.1612247398'
}

session = requests.Session()
session.headers = headers

re_jump = re.compile('//location.href="(.*)"')


def get_fangurl():
    
    base_url = 'https://gz.esf.fang.com'
    # 爬取每一页
    for i in range(1,2):
        url = 'https://gz.esf.fang.com/house-a078/i3{}'.format(quote(str(i)))
        jump_html = session.get(url)
        jump_url = re_jump.findall(jump_html.text)[0]
        html = session.get(jump_url)

        threadingpool = ThreadPoolExecutor(max_workers=10)
        soup = BeautifulSoup(html.text, 'lxml')
        hrefs = soup.select('dd .clearfix a')
        
        for href in hrefs:
            h = href['href']
            data_url = base_url + h
            #print(data_url)
            #get_data(data_url)
            threadingpool.submit(get_data, data_url)


def get_data(url):
    
    jump_html = session.get(url)
    jump_url = re_jump.findall(jump_html.text)[0]
    data_html = session.get(jump_url)

    sub_html = re.sub('<br>|<br />', '\n', data_html.text)
    soup = BeautifulSoup(sub_html, 'lxml')

    try:
        title = soup.select('h1 span')[0].text.strip()
        u_type = soup.select('.trl-item1.w146 .tt')[0].text.strip()
        area = soup.select('.trl-item1.w182 .tt')[0].text.strip()
        price = soup.select('.trl-item1.w132 .tt')[0].text.strip()
        year = soup.select('.text-item.clearfix .rcont')[0].text.strip()
        point = soup.select('.font14.hxmd .fyms_con')[0].text.strip()

        #print(title, u_type, area, price, year, point)
        #print('-*' * 20)
        data = Fang(title=title, unit_type=u_type, area=area, price=price,
                year=year, sale_point=point)

        sess.add(data)
        sess.commit()

    except Exception as e:
        print(e)
        sess.rollback()


if __name__ == '__main__':

    get_fangurl()


