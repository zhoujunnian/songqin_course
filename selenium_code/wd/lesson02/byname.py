# coding=utf8
from selenium import webdriver
import selenium

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson02/s1.html') # 打开网址

# -----------------------------------
try:
    ele = driver.find_element_by_name("button4")
except selenium.common.exceptions.NoSuchElementException:
    print('不存在')



# -----------------------------------


# raw_input('press any key to quit...')
driver.quit()

