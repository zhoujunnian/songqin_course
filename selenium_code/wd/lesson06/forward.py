# coding:utf8
from selenium import webdriver
import time

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)


driver.get('https://www.baidu.com/')
driver.find_element_by_id("kw").send_keys(u'松勤\n')
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()

input('...')
driver.quit()