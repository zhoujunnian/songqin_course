# coding=utf-8
from selenium import webdriver
import time

executable_path = r"d:\tools\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path)
driver.implicitly_wait(10)

driver.get('https://www.vmall.com/')

# ---------------------------------------

ele= driver.find_element_by_css_selector(
    '#zxnav_1 > div.category-panels  >ul >li >a')

ele.click()


# ---------------------------------------

input('press any key to quit...')
driver.quit()

