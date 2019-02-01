# coding=utf8
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson02/s1.html') # 打开网址


# -----------------------------------

ele = driver.find_element_by_link_text("转到百度")
ele.click()
# -----------------------------------
input('...')

driver.quit()   # 浏览器退出
