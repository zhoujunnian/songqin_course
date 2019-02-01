# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

# ----------------------------------
driver.get('http://check.ytesting.com')
driver.find_element_by_id('username').send_keys('sdfdsf')
driver.find_element_by_id('password').send_keys('sdfdsf')

time.sleep(2)
driver.refresh()


# ----------------------------------
input('press any key to quit...')
driver.quit()   # 浏览器退出