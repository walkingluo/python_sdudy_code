# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from requests.utils import quote
import json
import re


class CrawlJD():

    def __init__(self, keyword):

        self.keyword = keyword
        self.start_url = 'https://search.jd.com/Search?keyword={}&page='.format(quote(self.keyword))
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
            'cookie': 'pinId=u9LNDi_8jG3BykyFEUgMdrV9-x-f3wj7; shshshfpa=8210e55d-a425-057f-acfc-a7d677e32830-1531209696; shshshfpb=050886e6f724a7828b157e24897644558b5c9add59c51f6515b1354319; __jdu=984418612; qrsc=3; pin=jd_6b26b0eeddda0; unick=jd_jiangluo; _tp=tnT12zkUaeZvyImxEXopiLlGsyjvZAH5CmTXvHLsGPQ%3D; _pst=jd_6b26b0eeddda0; ipLocation=%u5e7f%u4e1c; UM_distinctid=1759282818f21-005d8e6aa864cc-303464-1fa400-17592828190123; user-key=964cd70b-dfaf-4610-bd37-f0086a0e75d7; shshshfp=49e5142c5e23129d127d664ba1220a4c; TrackID=1iA8Q1uCIxtMFHZzHNjDSwvPpUSaPWG-CKYV12J0JuwdI_1ooTDLOFL-dBNFCr5BW0JGeiXuOGmvctEwx0Mda5_-KnI5xO5Crn4IEnWB2-LQ; unpl=V2_ZzNtbRcFR0V8D0ZVf0pcUWIKRgkRVkUVdAsVVC4RXgxgAUJdclRCFnUUR1RnGlgUZwYZXkNcQxNFCEdkex5fDGQzEl9AVUscdgtEZEsaXDVmMxpUR1JDHHIIRWRLGVQBVzMiWkdQRRx8DUJkeildNSxtExBKXkYQdQFBVHgpXgVnABZtQQ%3d%3d; __jdv=122270672|c.duomai.com|t_16282_133398223|tuiguang|dc5a86105b1e48eeb07102b1d93863a1|1611555621184; cn=2; areaId=19; ipLoc-djd=19-1601-36953-0; __jdc=122270672; __jda=122270672.984418612.1539938182.1612086570.1612330018.361; CNZZDATA1256793290=1874759814-1604480779-https%253A%252F%252Fwww.jd.com%252F%7C1612328507; rkv=1.0; 3AB9D23F7A4B3C9B=YSMG6L5GJ4KTDNK3SBWGUUIAUSQU66LBJICUTNAEYCNIE4YSQ2K245BNYB5YZHROOCBEIWAD7LT3OZSGYFQA5IREKA; __jdb=122270672.4.984418612|361.1612330018; shshshsID=61f5895bb36cb1c20717917bdb845b45_4_1612330065440'
        }
        self.session = requests.Session()
        self.session.headers = self.headers

    def get_urls(self):

        url_list = []
        end_page = 2
        for i in range(1, end_page):
            url = self.start_url + str(i)
            url_list.append(url)
        return url_list
    
    def get_html(self, url):

        html = self.session.get(url)
        return html.text

    def parse_html(self, html):

        soup = BeautifulSoup(html, 'lxml')
        items = soup.select('.gl-item')
        print(len(items))
        for item in items[:2]:
            print('-*' * 20)
            title = item.select('.gl-i-wrap div.p-name a')[0].text.strip()
            price = item.select('.gl-i-wrap div.p-price strong')[0].text.strip()
            href = item.select('.gl-i-wrap div.p-img a')[0]['href']
            pid = re.search('\d+', href).group()
            print(pid)
            comment_num = self.get_comments(pid)
            print(title, price, comment_num)
            

    def run(self):

        # 网站每一页是按奇数递进的，每页有60项，实际爬取时可分成了2页，每页30项
        # https://search.jd.com/Search?keyword=python&page=1    page=2 为网页ajax后加载的
        # https://search.jd.com/Search?keyword=python&page=3    page=4 为网友ajax后加载的
        # 所以可按页顺序爬取， 每页30项
        url_list = self.get_urls()

        for url in url_list:

            html = self.get_html(url)
            self.parse_html(html)

    def get_comments(self, pid):

        ''' 获取商品评论 '''
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
            'Referer': 'https://item.jd.com/',
            'Cookie': 'pinId=u9LNDi_8jG3BykyFEUgMdrV9-x-f3wj7; shshshfpa=8210e55d-a425-057f-acfc-a7d677e32830-1531209696; shshshfpb=050886e6f724a7828b157e24897644558b5c9add59c51f6515b1354319; __jdu=984418612; pin=jd_6b26b0eeddda0; unick=jd_jiangluo; _tp=tnT12zkUaeZvyImxEXopiLlGsyjvZAH5CmTXvHLsGPQ%3D; _pst=jd_6b26b0eeddda0; ipLocation=%u5e7f%u4e1c; UM_distinctid=176b7fca2602e7-0677e2cb3989f5-c791039-1fa400-176b7fca2616d7; CNZZDATA1256793290=1132259995-1609401621-https%253A%252F%252Fwww.google.com%252F%7C1609401621; user-key=964cd70b-dfaf-4610-bd37-f0086a0e75d7; shshshfp=49e5142c5e23129d127d664ba1220a4c; TrackID=1iA8Q1uCIxtMFHZzHNjDSwvPpUSaPWG-CKYV12J0JuwdI_1ooTDLOFL-dBNFCr5BW0JGeiXuOGmvctEwx0Mda5_-KnI5xO5Crn4IEnWB2-LQ; unpl=V2_ZzNtbRcFR0V8D0ZVf0pcUWIKRgkRVkUVdAsVVC4RXgxgAUJdclRCFnUUR1RnGlgUZwYZXkNcQxNFCEdkex5fDGQzEl9AVUscdgtEZEsaXDVmMxpUR1JDHHIIRWRLGVQBVzMiWkdQRRx8DUJkeildNSxtExBKXkYQdQFBVHgpXgVnABZtQQ%3d%3d; __jdv=122270672|c.duomai.com|t_16282_133398223|tuiguang|dc5a86105b1e48eeb07102b1d93863a1|1611555621184; cn=2; areaId=19; ipLoc-djd=19-1601-36953-0; __jdc=122270672; 3AB9D23F7A4B3C9B=YSMG6L5GJ4KTDNK3SBWGUUIAUSQU66LBJICUTNAEYCNIE4YSQ2K245BNYB5YZHROOCBEIWAD7LT3OZSGYFQA5IREKA; __jda=122270672.984418612.1539938182.1612330018.1612334653.362; jwotest_product=99; shshshsID=88d6abf55a520ef393dd11135ccba7cc_2_1612334686450; __jdb=122270672.2.984418612|362.1612334653; JSESSIONID=EF017F8B2F7E159720A97D5EC2C314D0.s1'}

        page = 2
        for i in range(page):

            url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&rid=0&fold=1'.format(pid, i)
            comm = requests.get(url, headers=header)

            result = self.get_json(comm.text)
            if i == 0:
                comment_num = result['productCommentSummary']['commentCount']
            comments = result['comments']

            print('---第{}页---'.format(i+1))
            for comment in comments:
                print(comment['content'])

        return comment_num

    def get_json(self, text):

        start = text.find('{"productAttr":null')
        end = text.find('}]}') + len('}]}')
        result = json.loads(text[start:end])

        return result
            

if __name__ == '__main__':

    crawl = CrawlJD('python')
    crawl.run()