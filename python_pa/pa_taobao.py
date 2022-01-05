# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from bs4 import BeautifulSoup
import time


KEYWORD = 'python'
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


def cawl_page(page):
    
    try:
        # 传参
        # params = {'q': KEYWORD}
        # url = "https://s.taobao.com/search"
        # driver.get(url, params=params)
        url = "https://s.taobao.com/search?q=" + quote(KEYWORD)  # 中文的需要quote解析
        driver.get(url)
        time.sleep(5)
        if page > 1:
            page_label = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '#mainsrp-pager .form .input.J_Input')
                )
            )

            submit_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, '#mainsrp-pager .form .btn.J_Submit')
                )
            )

            page_label.clear()
            page_label.send_keys(page)
            submit_button.click()
            
        # 经测试，滑动到3000可以获取全部图片链接！
        driver.execute_script("window.scrollTo(0, 3000);")
        # 10s内定位，失败报错
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.m-itemlist .items .item')
            )
        )

        get_products()
    except:
        pass
        cawl_page(page)


def get_products():
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    #print(soup.prettify())
    items = soup.select('#mainsrp-itemlist .items .item')
    products = []
    for item in items:
        #print(item)
        products.append({
            'img': item.select('.J_ItemPic.img')[0]['src'],
            'price': item.select('.price')[0].text.strip(),
            'deal': item.select('.deal-cnt')[0].text.strip(),
            'title': item.select('.title')[0].text.strip(),
            'shop': item.select('.shopname')[0].text.strip(),
            'location': item.select('.location')[0].text.strip()
        })
        #print(products[-1])

    with open('./python_pa/taobao.txt', 'w+', encoding='utf-8') as f:
        for p in products:
            values = ''
            for v in p.values():
                values += v + ','
            #print(values)
            f.writelines(values)
            f.writelines('\n')


if __name__ == '__main__':

    cawl_page(1)
