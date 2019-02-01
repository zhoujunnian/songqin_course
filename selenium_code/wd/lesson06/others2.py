# coding:utf8
from selenium import webdriver
executable_path = r"d:\tools\webdrivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path)

driver.implicitly_wait(10)

import time
driver.get('https://kyfw.12306.cn')
driver.find_element_by_css_selector('#selectYuding>a').click()

time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()


driver.quit()