# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

url = 'https://gz.esf.fang.com/house-a078/i31'

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'cookie': 'city=gz; global_cookie=8to28852tyw7c43x41v3dju5k17kknmgsrb; __utma=147393320.56836883.1612247398.1612247398.1612247398.1; __utmc=147393320; __utmz=147393320.1612247398.1.1.utmcsr=gz.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/; showCity=b"\xc3\xa5\xc2\xb9\xc2\xbf\xc3\xa5\xc2\xb7\xc5\xbe"; newhouse_user_guid=4F4C4ED9-FA27-8357-0B96-C1C2E5E35D4D; newhouse_chat_guid=C50A1848-961D-01A4-27CF-223182592717; csrfToken=Cgp18ZTDEQI9yPMG8L848OV8; lastscanpage=0; g_sourcepage=esf_fy%5Elb_pc; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; unique_cookie=U_8to28852tyw7c43x41v3dju5k17kknmgsrb*18; __utmb=147393320.57.10.1612247398'
}

#html = requests.get(url, headers=headers)
#print(html.text)
re_jump = re.compile('//location.href="(.*)"')
#jump_url = re_jump.findall(html.text)[0]

#jump_html = requests.get(jump_url, headers=headers)
#print(jump_html.text)
'''
soup = BeautifulSoup(jump_html.text, 'lxml')
#print(soup.title)
hrefs = soup.select('dd .clearfix a')
base_url = 'https://gz.esf.fang.com'
for href in hrefs:
    h = href['href']
    u = base_url + h
    print(u)
'''

d_url = 'https://gz.esf.fang.com/chushou/3_252819539.htm'
html = requests.get(d_url, headers=headers)
#print(html.text)
jump_url = re_jump.findall(html.text)[0]
jump_html = requests.get(jump_url, headers=headers)
#print(jump_html.text)
# with open('./python_pa/fangtianxia/index.html', 'w', encoding='utf-8') as f:
#     f.write(jump_html.text)
s = re.sub('<br>|<br />', '\n', jump_html.text)
soup = BeautifulSoup(s, 'lxml')
# title = soup.select('h1 span')[0].text.strip()
# u_type = soup.select('.trl-item1.w146 .tt')[0].text.strip()
# area = soup.select('.trl-item1.w182 .tt')[0].text.strip()
# price = soup.select('.trl-item1.w132 .tt')[0].text.strip()
# year = soup.select('.text-item.clearfix ,rcont')[0].text.strip()
point = soup.select('.font14.hxmd .fyms_con')[0].text.strip()
# print(title)
# print(u_type)
# print(area)
# print(price)
# print(year)
print(point)



