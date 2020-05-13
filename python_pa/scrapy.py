# -*- coding:utf-8 -*-

import requests
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.zhihu.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/80.0.3987.132 Safari/537.36'}                    
cookie = {'cookie':'_zap=1e93b070-8221-438e-bada-8a8abd4e913a; _xsrf=vpzSWEDzI1mcQcbnnuEUq34KMzmH3Rzk; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1583833123; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1583833123; d_c0="ACCbWo0H8RCPTjKDKDx6VyenOeWXhrPyblk=|1583833122"; _ga=GA1.2.921356637.1583833123; _gid=GA1.2.844489075.1583833123; _gat_gtag_UA_149949619_1=1; capsion_ticket="2|1:0|10:1583833131|14:capsion_ticket|44:ZGVkYmQ4MWMxZDJmNDJkZGIzNTRiY2JiMDFlNTA0MWU=|f510032a91069a2f633374384c1deb8ce97286bd4cf945a77bd818521fd7224c"; KLBRSID=2177cbf908056c6654e972f5ddc96dc2|1583833131|1583833121'}
session = requests.Session()
html = session.get(url, headers=headers, cookies=cookie).content
print(len(html))
with open('file.txt', 'wb') as f:
	f.write(html)
'''
request = urllib.request.Request(url=url, headers=header)
response = urllib.request.urlopen(request)
print(response.getcode())    #获取状态码，200表示成功
html = response.read()
print(len(html))    #网页内容长度
'''
'''
soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
cityname = soup.find('div', class_='css-1pysja1')
print(cityname)'''
'''
cityname = 'https:' + cityname['src']

with open('logo.png', 'wb') as f:
	png = requests.get(cityname)
	#f.write(png.content)
print('done')
'''