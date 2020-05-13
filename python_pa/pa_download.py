# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

URL = "http://www.nationalgeographic.com.cn/animals/"

html = requests.get(URL).text
soup = BeautifulSoup(html, features='lxml')
img_ui =  soup.find_all('ul', {'class':'img_list'})
for ui in img_ui:
    imgs = ui.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print("Saved %s" % image_name)