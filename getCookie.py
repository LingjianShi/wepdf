# -*- coding:utf-8 -*-

from selenium import webdriver
import time
import json
from pprint import pprint
 
post = {}
 
#driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver = webdriver.Chrome()
driver.get('https://mp.weixin.qq.com/')
time.sleep(2)
driver.find_element_by_xpath("./*//input[@name='account']").clear()
driver.find_element_by_xpath("./*//input[@name='account']").send_keys('********')
driver.find_element_by_xpath("./*//input[@name='password']").clear()
driver.find_element_by_xpath("./*//input[@name='password']").send_keys('********')
# <label class="frm_checkbox_label">
# <label class="frm_checkbox_label selected">
# 在自动输完密码之后记得点一下记住我
time.sleep(5)
driver.find_element_by_xpath("./*//a[@title='点击登录']").click()
# 拿手机扫二维码！
time.sleep(15)
driver.get('https://mp.weixin.qq.com/')
cookie_items = driver.get_cookies()
for cookie_item in cookie_items:
    post[cookie_item['name']] = cookie_item['value']
cookie_str = json.dumps(post)
with open('cookie.txt', 'w+') as f:
    f.write(cookie_str)