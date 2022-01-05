# -*- coding:utf-8 -*-

import asyncio
import aiohttp
from bs4 import BeautifulSoup
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
    'cookie': '__DAYU_PP=6EF7NAmrj3IyrrIjqiUi20d22e24c970; _zap=2e7f4389-95df-4a61-98f5-cd79f379e195; _ga=GA1.2.978450062.1582966942; d_c0="AMDT99kGRRKPTlcScUKP8b9UVyDV96YQTfc=|1606649952"; z_c0="2|1:0|10:1609255647|4:z_c0|92:Mi4xQzI2bkFBQUFBQUFBd05QMzJRWkZFaVlBQUFCZ0FsVk4zNWpZWUFDVG9BSm1PSkFQalRadlVxLWFlQVBkX3hoZUVB|a0ada397eb86978f6f250419265d72ac9685d4c86490a8cecfb7b64b53e4b1e2"; q_c1=3d242fee0dbf4ee5b4098b6cb2c78349|1610467882000|1508989904000; ISSW=1; _xsrf=74839649-81f2-443d-802d-1ded4a6718b6; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1611994008,1612073200,1612111319,1612166929; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1612166929; SESSIONID=lFdfQP9ekHkNuEqi5XSBSsdgVGA8SJIjaD88cRmsSYq; KLBRSID=0a401b23e8a71b70de2f4b37f5b4e379|1612166931|1612166926; JOID=WlgTA0_rpddfa9N0e-MRQOrKHS5kj-W1PTaLSxiM5boXGpoNFPYSwjdv3XR5xlS5gzpJkuiNKW5mDacslfMOQg4=; osd=V1wXAkrmodNebt5wf-IUTe7OHCtpi-G0ODuPTxmJ6L4TG58AEPITxzpr2XV8y1C9gj9EluyMLGNiCaYpmPcKQws='
}

ids = re.compile('"cardId":"Q_(\d+)"')

async def crawl():

    url = 'https://www.zhihu.com/billboard'

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as res:
            print(res.status)
            html = await res.text()

    soup = BeautifulSoup(html, 'lxml')
    items = soup.select('.HotList-item')
    for item in items:
        title = item.select('.HotList-itemTitle')[0].text
        hot = item.select('.HotList-itemMetrics')[0].text
        print(title, hot)
        
    hot_ids = ids.findall(html)
    print(hot_ids)

def main():

    loop = asyncio.get_event_loop()
    loop.run_until_complete(crawl())
    loop.close()

if __name__ == '__main__':

    main()