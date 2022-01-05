# -*- coding:utf-8 -*-

import requests
from urllib.parse import quote
from uuid import uuid4
from multiprocessing import current_process
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

headers = {'User-Agent': 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
            'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E7%99%BE%E5%BA%A6%E5%9B%BE%E7%89%87',
            'Cookie': 'BIDUPSID=468398B63E2587B44716D9D79FA840EE; PSTM=1508494231; H_WISE_SIDS=154758_153758_155181_155443_149355_156818_156286_150775_154259_155985_148865_154605_157762_153715_156623_157262_146871_154771_150772_151015_156388_156579_156516_127969_153144_154175_155963_152981_154013_146732_156245_155791_131423_128701_155529_107319_156216_154189_156943_155344_154776_158026_151871_144966_156521_154619_139883_156099_158088_156293_147551_156104_158126_157696_154639_152310_154353_110085_157006; __yjs_duid=1_c14edd357e4bf203db63b9ae2fde31391609220155343; BAIDUID=E4E3C49F2EBF1302DF13DE6AF79F77A8:FG=1; BDUSS=cyTENmQ2ZQd0c5cDJ1Zk80TVB4cy1Nbm5DdlRxSUE5NDRoNXI3bWFzWHVUU2xnSVFBQUFBJCQAAAAAAAAAAAEAAACO7OAfcm9qb2UxOTkxMTIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO7AAWDuwAFgQj; BDUSS_BFESS=cyTENmQ2ZQd0c5cDJ1Zk80TVB4cy1Nbm5DdlRxSUE5NDRoNXI3bWFzWHVUU2xnSVFBQUFBJCQAAAAAAAAAAAEAAACO7OAfcm9qb2UxOTkxMTIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO7AAWDuwAFgQj; H_PS_PSSID=33423_33354_33344_31660_33162_26350_33567; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BAIDUID_BFESS=E4E3C49F2EBF1302DF13DE6AF79F77A8:FG=1; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; ab_sr=1.0.0_MGI4ZWYzZGUzYTE4NWZhY2FjOWNlYmJkMWMyZjQwYTcyODUyYTQ0ZGQ1ZDQzZWQ3ODk3NTM4MTQ5OWQxMDQxMWZjYThiYWQyOWM1OWExYTVhMDU5NTU0OWMwMTBjZGM5N2QxYzI5MjgyMjIyYzg1M2I0ZjU4ZGY5NGNlM2RiMDk='}

# ip代理
proxies = {
    'http': 'http://171.13.136.161:9999',
    'https': 'http://171.13.136.161:9999'
}

# 使用session会话，一次连接，多次请求资源
session = requests.Session()
session.headers = headers
#session.proxies = proxies


def get_img(url):
    #html = requests.get(url, headers=headers)
    html = session.get(url)
    html.encoding = 'utf-8'
    print('当前进程PID: {}'.format(current_process().pid))
    threadpools = ThreadPoolExecutor(max_workers=5)
    content = html.json()['data']
    for c in content[:-1]:
        # print(c['middleURL'])
        link = c['middleURL']
        threadpools.submit(download_img, link)


def download_img(url):
    #img = requests.get(url, headers=headers)
    img = session.get(url)
    print('Downloading . . . {}'.format(img.url))
    with open('./python_pa/baidu_img/{}.jpg'.format(uuid4()), 'wb') as f:
        for chunk in img.iter_content(chunk_size=128):
            if chunk:
                f.write(chunk)


def test_json(url):
    #html = requests.get(url, headers=headers)
    html = session.get(url, timeout=1)
    html.encoding = 'utf-8'
    content = html.json()['data']
    print(content[0]['middleURL'])


if __name__ == '__main__':

    keyword = '海贼王'
    s = time.time()
    for i in range(30, 150, 30):
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&z=&ic=&hd=&latest=&copyright=&word={}&s=&se=&tab=&width=&height=&face=&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30'.format(quote(keyword), quote(keyword), i)
        get_img(url)
    print(time.time()-s)
    # test_json(url)