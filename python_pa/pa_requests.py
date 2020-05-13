# -*- coding:utf-8 -*-

import requests
import webbrowser
import os
from urllib.request import urlretrieve

base_url = 'http://www.baidu.com/s'
param = {'wd': 'python'}
r = requests.get(base_url, params=param)
print(r.url)
#webbrowser.open(r.url)
'''
data = {'firstname':'123', 'lastname':'456'}
r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
print(r.text)
'''
'''
upfile = {'uploadFile':open('./1.jpg','rb')}
r = requests.post('http://pythonscraping.com/pages/files/processing2.php', files=upfile)
print(r.text)
'''
'''
session = requests.Session()
payload = {'username':'aaa', 'password':'password'}
r = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
print(r.cookies.get_dict())

r = session.get('http://pythonscraping.com/pages/cookies/profile.php')
print(r.url)
'''
'''
os.makedirs('./img/', exist_ok=True)
IMAGE_URL = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'
#urlretrieve(IMAGE_URL, './img/image1.png')

r = requests.get(IMAGE_URL)
with open('./img/image3.png', 'wb') as f:
    #f.write(r.content)
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
'''
