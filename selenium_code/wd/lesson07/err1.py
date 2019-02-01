# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson07/ac.html')




t1 = driver.find_element_by_id('1t')
t2 = driver.find_element_by_id('t2')
t3 = driver.find_element_by_id('n3')





driver.quit()

