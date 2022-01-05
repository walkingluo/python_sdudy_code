# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


def test_webdriver():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    search_box = driver.find_element_by_id('kw')
    search_box.send_keys('python')
    time.sleep(2)
    submit_button = driver.find_element_by_id('su')
    submit_button.click()
    time.sleep(2)

def test():

    driver = webdriver.Chrome()
    driver.get("https://www.135editor.com/pictures.html?page=1")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 1000);")
    element = driver.find_element_by_xpath('//*[@id="content-0"]')
    content = element.find_elements_by_tag_name('img')
    #print(content.get_attribute('outerHTML'))
    for c in content:
        print(c.get_attribute('outerHTML'))
    

def get_img():
    URL = "https://www.135editor.com/pictures.html?page=2"

    html = requests.get(URL).content
    soup = BeautifulSoup(html, features='lxml')
    img_ui = soup.find_all('img')
    print(len(img_ui))
    print(img_ui)
    '''
    for ui in img_ui:
        url = ui['src']
        try:
            r = requests.get(url, stream=True)
            image_name = url.split('/')[-1]
            with open('./python_pa/img/%s' % image_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=128):
                    f.write(chunk)
        except:
            pass
        print("Saved %s" % image_name)
    '''

if __name__ == '__main__':
    #test()
    test_webdriver()