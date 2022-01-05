# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os
from doubandb import Book, sess

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'Cookie': 'douban-fav-remind=1; _vwo_uuid_v2=DDCE776F9911CC84C91C4AB3BE6CC6600|47ea7e16b25d0c7f535ca5d4c5ccd6cd; ll="118281"; bid=FKSU7PLQgc0; gr_user_id=41f66bb1-6d17-4434-8494-22d53e620d50; viewed="19952400_3852290_26708119"; _ga=GA1.2.506283143.1510730021; push_doumail_num=0; push_noty_num=0; dbcl2="119655579:ePjecCO3UEw"; __utmv=30149280.11965; douban-profile-remind=1; __utmz=81379588.1611216247.1.1.utmcsr=nndl.github.io|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=30149280.1611761628.71.48.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ck=qWES; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=f33337e4-aff2-45ed-a2cf-3e3ac4d99a5c; gr_cs1_f33337e4-aff2-45ed-a2cf-3e3ac4d99a5c=user_id%3A1; ap_v=0,6.0; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1611810493%2C%22https%3A%2F%2Fnndl.github.io%2F%22%5D; _pk_ses.100001.3ac3=*; __utma=30149280.506283143.1510730021.1611761628.1611810493.72; __utmc=30149280; __utmt_douban=1; __utma=81379588.506283143.1510730021.1611216247.1611810493.2; __utmc=81379588; __utmt=1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_f33337e4-aff2-45ed-a2cf-3e3ac4d99a5c=true; __utmb=30149280.6.10.1611810493; __utmb=81379588.6.10.1611810493; _pk_id.100001.3ac3=94d1b447434472e7.1611216246.2.1611810541.1611216301.'
}

session = requests.Session()
session.headers = headers

def get_douban_book():

    # 翻页，每20为一页
    for i in range(0, 20, 20):

        url = 'https://book.douban.com/tag/%E9%9A%8F%E7%AC%94?start={}&type=T'.format(i)
        html = session.get(url).text

        soup = BeautifulSoup(html, 'lxml')
        books = soup.select('.subject-item')
        for book in books:
            try:
                book_name = book.select_one('.info h2 a').text.strip().replace(' ', '').replace('\n', '')
                book_info = book.select_one('.info .pub').text.strip().replace(' ', '').replace('\n', '')
                book_intro = book.select_one('.info p').text.strip().replace(' ', '').replace('\n', '')
                book_rating_num = book.select_one('.star.clearfix .rating_nums').text.replace(' ', '').replace('\n', '')
                book_rating_people = book.select_one('.star.clearfix .pl').text.replace(' ', '').replace('\n', '')
                # book_img = book.select_one('.pic img')['src']
                
                # download_img(book_name, book_img)
                # print(book_name, book_info, book_intro, book_rating_num, book_rating_people)

                # 插入数据库
                book_data = Book(
                    name=book_name, info=book_info, intro=book_intro, 
                    rating_num=book_rating_num, rating_people=book_rating_people
                )

                sess.add(book_data)
                sess.commit()
            except Exception as e:
                print(e)
                sess.rollback()


def download_img(name, img_url):

    if not os.path.exists('./python_pa/douban_img'):
        os.mkdir('./python_pa/douban_img')

    img = session.get(img_url)
    with open('./python_pa/douban_img/{}.jpg'.format(name), 'wb') as f:
        for chunk in img.iter_content(chunk_size=128):
            if chunk:
                f.write(chunk)


if __name__ == '__main__':

    get_douban_book()