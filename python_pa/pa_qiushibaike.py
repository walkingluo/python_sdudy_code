# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import sys

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}


def cawl_duanzi(url):
    
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    try:
        duanzi_text = soup.select('.content')[0].text
        duanzi_author = soup.select('.side-user-name')[0].text
        duanzi_message = soup.select('.side-detail')
        tag_num = ''
        for m in duanzi_message:
            tag = m.select('.side-line2')[0].text
            num = m.select('.side-line1')[0].text
            tag_num += tag + ':' + num + ' '
        print(duanzi_text)    
        
        with open('./python_pa/qiushibaike.txt', 'a+', encoding='utf-8') as f:        
            f.writelines("{};{};{}\n".format(duanzi_text, duanzi_author, tag_num))
            
    except:
        print(url)
        print("Unexpected error:", sys.exc_info()[0])
        cawl_duanzi(url)   # 出错重新执行
        

def qiushi_duanzi():
    # 翻页
    for i in range(1,2):
        url = "https://www.qiushibaike.com/text/page/{}/".format(i)
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, 'lxml')
        duanzi_url = soup.select('.article.block.untagged.mb15')
        print(len(duanzi_url))
        for h in duanzi_url:
            new_url = h.select('.contentHerf')[0]['href']
            full_url = "https://www.qiushibaike.com" + new_url
            cawl_duanzi(full_url)


def test_soup():
    url = "https://www.qiushibaike.com/text/"
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    #print(soup.title)
    #print(soup.head)
    #print(soup.a)  # 找到第一个a
    # find 为搜索， select为css选择器
    #print(soup.find_all('a'))  # 找到所有a
    #print(soup.find_all(True, class_='content'))  # class为python保留字，需要加_ 找到所有class='content'
    #print(soup.select('.content'))  # .代表class， #代表id, 也是找到所有class='content'
    #print(soup.select('.content > span')) # 找到.content的直接子标签


if __name__ == '__main__':

    #url = "https://www.qiushibaike.com/article/123830372"
    #cawl_duanzi(url)
    qiushi_duanzi()
    #test_soup()