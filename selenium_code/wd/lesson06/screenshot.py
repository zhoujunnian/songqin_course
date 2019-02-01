# coding=utf-8
from selenium import webdriver
import  time


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('https://www.sohu.com')


# ----------------------------------
driver.get_screenshot_as_file('shot11.png')
#
# ele = driver.find_element_by_id('search')
# ele.screenshot_as_png('search.png')
# ----------------------------------
input('press any key to quit...')
driver.quit()   # 浏览器退出