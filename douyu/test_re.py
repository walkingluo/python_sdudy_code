import hashlib
import re
import time

import execjs
import requests


def test_re():

    rid = 288016
    t10 = str(int(time.time()))
    t13 = str(int(time.time() * 1000))
    print(t10)
    print(t13)

    s = requests.Session()
    res = s.get('https://m.douyu.com/' + str(rid)).text
    #result = re.search(r'rid":(\d{1,7}),"vipId', res)
    #print(result.group(1))
    result = re.search(r'(function ub98484234.*)\s(var.*)', res).group()
    func_ub9 = re.sub(r'eval.*;}', 'strc;}', result)    #第二个参数替换第一个参数的内容
    #print(func_ub9)
    js = execjs.compile(func_ub9)
    res = js.call('ub98484234')
    v = re.search(r'v=(\d+)', res).group(1)
    print(v)


if __name__ == '__main__':
    test_re()