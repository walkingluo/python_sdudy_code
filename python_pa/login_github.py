# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time

headers = {
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
  'referer': 'https://github.com/login',
  'cookie': '_ga=GA1.2.518090083.1508498620; _device_id=f5747fbb1b7c9fbbefbe2cb353c9bd3f; _octo=GH1.1.1402525845.1571895574; has_recent_activity=1; tz=Asia%2FShanghai; logged_in=no; _gh_sess=HBLBLWu7GETsDQIdMj6yXf2cuwmgpBMQfwYH158FTvzSi30Gsjnr%2FxSiOmyHTKE0oQFpHylQSvOZvFVn%2Fpgv96pFfxigQ%2Fp4%2Bcsubse6SXwr9Sd09HN5tNMKkNNWnGk%2FxiRkbBP8cYqhCybH7mr87nwU8iqzPDJSrbkAQBPvTSmCc%2FbqU1%2FlubGgz611792bgA%2B992RGKDgA%2B8R80Lvl94WIhUxnpdXq98GDir%2FkLdUvOpOrMVCLP9XvFVi07n48o0twgzC0if69Jm7C07vUUw%3D%3D--gDP1nC2vYDhmh%2F5H--%2FO9Lp2WZliq0AR%2BA%2FL64gA%3D%3D'
}

sess = requests.session()
sess.headers = headers


def save_html(html):

    with open('./python_pa/github.html', 'w+', encoding='utf-8') as f:
        f.write(html)


def get_feed(session):

    url = "https://github.com/dashboard-feed"
    html = session.get(url)
    soup = BeautifulSoup(html.text, 'lxml')

    feed = soup.select('.Box.p-5.mt-3 h2')[0].text
    print(feed)
    '''
    for f in feeds:
        content = f.select('a')[0].text
        print(content)
    '''

def login():
    url = 'https://github.com/session'
    data = {
        'commit': 'Sign in',
        'authenticity_token': 'Os1CNtv7GwBjo+xmp5TTU8ZcBY7MLcVash0r7Wo96gYY5weJK1b9pFc8FMl4e3h13wFACb+Z9X9EWcbQ3Otm+w==',
        'login': 'rojoe07@gmail.com',
        'password': 'ro19911231,.',
        'webauthn-support': 'supported',
        'webauthn-iuvpaa-support': 'supported',
        'timestamp': '{}'.format(time.time()),
        'timestamp_secret': '7672b373c1242c39c4a6f3378b3f565ad7982926de5ceb4a0fd5d9e5b8e15bd2'
    }

    html = sess.post(url, data=data)
    if html.status_code == 200:
        print("访问成功！")
        save_html(html.text)
        get_feed(sess)
    else:
        print("登录失败！")


def test_time():

    print(time.time())


if __name__ == '__main__':

    login()
    #test_time()

