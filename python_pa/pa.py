# -*- coding:utf-8 -*-

from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
'''
html = urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html"
    ).read().decode('utf-8')
#print(html)
html_css = urlopen(
    "https://morvanzhou.github.io/static/scraping/list.html"
    ).read().decode('utf-8')
#print(html_css)
'''
html_re = urlopen(
    "https://morvanzhou.github.io/static/scraping/table.html"
    ).read().decode('utf-8')
#print(html_re)
'''
res = re.findall(r"<title>(.+?)</title>", html)
print("Page title is:", res[0])

res = re.findall(r"<p>(.+?)</p>", html, flags=re.DOTALL)
print("Page paragraph is:", res[0])

res = re.findall(r'href="(.*?)"', html)
print("All links:", res)
'''
soup = BeautifulSoup(html_re, features='lxml')
#print(soup.h1)
#print(soup.p)
'''
all_href = soup.find_all('a')
all_href = [l['href'] for l in all_href]
print(all_href)
'''
'''
month = soup.find_all('li', {"class":"month"})
for m in month:
    print(m.get_text())

jan = soup.find('ul', {"class":"jan"})
d_jan = jan.find_all('li')
for d in d_jan:
    print(d.get_text())
'''

img_links = soup.find_all('img', {"src":re.compile(r'.*?\.jpg')})
for link in img_links:
    print(link['src'])

course_links = soup.find_all('a', {'href':re.compile(r'https://morvan.*')})
for link in course_links:
    print(link['href'])