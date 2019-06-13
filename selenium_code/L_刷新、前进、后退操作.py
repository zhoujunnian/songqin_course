# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('file:///Users/zhoujunjun/PycharmProjects/PycharmData/git_hub/songqin_course/selenium_code/html/s1.html')

# ----------------------------------
driver.get('http://check.ytesting.com')
driver.find_element_by_id('username').send_keys('sdfdsf')
driver.find_element_by_id('password').send_keys('sdfdsf')

time.sleep(2)
driver.refresh()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()

driver.get_screenshot_as_file('shot11.png')
# ----------------------------------
input('press any key to quit...')
driver.quit()   # 浏览器退出