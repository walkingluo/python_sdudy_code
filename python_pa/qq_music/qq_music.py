# -*- coding:utf-8 -*- 

from urllib import parse
import requests
from bs4 import BeautifulSoup
from requests.utils import quote
import math

headers = {
    'Referer': 'https://y.qq.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}


def get_page():

    # A-Z # 28个分类
    pages = []
    singer = {}
    for i in range(1,2):
        data = '{"comm":{"ct":24,"cv":0},"singerList":{"module":"Music.SingerListServer","method":"get_singer_list","param":{"area":-100,"sex":-100,"genre":-100,"index":%s,"sin":0,"cur_page":1}}}' % str(i)
        # 需要破解sign值  这个sign对应 A的第1页
        url = 'https://u.y.qq.com/cgi-bin/musics.fcg?-=getUCGI0679231540697367&g_tk=5381&sign=zzajra07y4mrvrgmog9395b8f02929008a5f659a04d02802de&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={}'.format(quote(data))

        html = requests.get(url).json()
        total = html['singerList']['data']['total']
        singer_list = html['singerList']['data']['singerlist']
        for i in range(80):
            singer_name = singer_list[i]['singer_name']
            singer_mid = singer_list[i]['singer_mid']
            singer.update({singer_name:singer_mid})
        pages.append(math.floor(int(total) / 80) + 1)
    
    return pages, singer

def get_singermid():

    # 同上需破解sign，才能获取
    # 获取到singermid后
    # url = 'https://u.y.qq.com/cgi-bin/musics.fcg?-=getSingerSong6685932300958888&g_tk=5381&sign=zzaxv25pewwrd8d2a50c382e8f04b4c0a280cbf931b24df&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data='
    # 根据singermid，代入data数据
    # 这里也需要破解歌手页的sign，才能获取数据
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'referer': 'https://y.qq.com/'
    }
    _, singer_mid = get_page()
    # 通过名字查找singermid
    print(singer_mid["Aron's Crusade"])
    # 每个歌手有不同的 sign
    data = '{"comm":{"ct":24,"cv":0},"singerSongList":{"method":"GetSingerSongList","param":{"order":1,"singerMid":"%s","begin":0,"num":10},"module":"musichall.song_list_server"}}' % singer_mid["Aron's Crusade"]
    url = 'https://u.y.qq.com/cgi-bin/musics.fcg?-=getSingerSong5061737931202559&g_tk=269699280&sign=zzalypl616pt35qk2a50c382e8f04b4c0a280cbf931b24df&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={}'.format(quote(data))
    
    html = requests.get(url).json()
    song_totalnum = html['singerSongList']['data']['totalNum']
    print(song_totalnum)
    songs = html['singerSongList']['data']['songList']
    for i in range(10):
        name = songs[i]['songInfo']['name']
        print(name)


if __name__ == '__main__':

    get_singermid()



