# -*- coding:utf-8 -*-

import re
import requests
from lxml import etree


def test_utf_8():

    str = "严"

    str_code = str.encode('utf-8')

    str_decode = str_code.decode('utf-8')

    print(str)
    print(str_code)
    print(str_decode)

    # 写入文件乱码  设置encoding='utf-8'
    # 获取网页乱码  设置html.encoding='utf-8'


def test_re():

    text = "<a href='https://www.baidu.com' href='https:/www.163.com'> python </a>"

    r = re.compile("href='(.*?)'", re.I | re.S)

    #result = re.match("<a href='.*?'", text, re.I | re.S)
    #result = re.search("href='(.*?)'", text, re.I | re.S)
    result = r.search(text)
    result_all = r.findall(text)   # 返回list
   
    print(result)
    print(result.group())  # 匹配的正则字符串 href='https://www.baidu.com'
    print(result.groups()) # 包含的字符串元组 ('https://www.baidu.com',) 
    print(result_all)

    # 替换
    text_sub = re.sub('href', 'url', text)
    print(text_sub)

    # email 正则  [^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+    ( ' '=space \t=tab \r=enter \n=newline)


def test_xpath():

    url = 'http://www.baidu.com/s?wd=pyhon'
    html = requests.get(url)

    result = etree.HTML(html.text)
    infos = result.xpath('//div[@id="content_left"]/div[contains(@class, "result")]')
    for info in infos:
        title = info.xpath('h3/a/text()')
        print(title)
        

if __name__ == '__main__':

    #test_re()
    test_xpath()