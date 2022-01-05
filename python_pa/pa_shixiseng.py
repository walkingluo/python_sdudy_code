# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

def decode_num():
    # 180
    print(''.encode('utf-8'))
    #
    # 0 \xef\x9d\xbe
    # 1 \xee\xb2\xa1
    # 2 \xef\x80\xbd
    # 3 \xef\x9d\x8e
    # 5 \xee\xaf\xa9
    # 8 \xef\x91\x82


def job_message(url):
    html = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('.new_job_name')[0].text
    company_name = soup.select('.com_intro .com-name')[0].text
    job_money = soup.select('.job_money.cutom_font')[0].text.encode('utf-8')
    job_money = job_money.replace(b'\xef\x9d\xbe', b'0')
    job_money = job_money.replace(b'\xee\xb2\xa1', b'1')
    job_money = job_money.replace(b'\xef\x80\xbd', b'2')
    job_money = job_money.replace(b'\xef\x9d\x8e', b'3')
    job_money = job_money.replace(b'\xee\xaf\xa9', b'5')
    job_money = job_money.replace(b'\xef\x91\x82', b'8')
    job_money = job_money.decode()
    print(title, company_name, job_money)

def shixi_page():

    for i in range(1,2):
        url = "https://www.shixiseng.com/interns?page={}&type=intern&keyword=python".format(i)
        html = requests.get(url, headers=headers).content
        soup = BeautifulSoup(html, 'lxml')
        job_name = soup.select('.intern-wrap.intern-item')
        for job in job_name[:5]:
            job_url = job.select('.f-l.intern-detail__job a')[0]['href']
            job_message(job_url)


if __name__ == '__main__':

    shixi_page()
    #decode_num()