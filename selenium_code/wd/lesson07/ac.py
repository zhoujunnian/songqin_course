# coding=utf-8
from selenium import webdriver
import time


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")


driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson07/ac.html')

# ---------------------------------------
from selenium.webdriver.common.action_chains import ActionChains

ac = ActionChains(driver)


t1 = driver.find_element_by_id('t1')
t2 = driver.find_element_by_id('t2')
t3 = driver.find_element_by_id('t3')


ac.click(t1).send_keys('1').click(t2).send_keys('2').click(t3).send_keys('3')\
    .perform()




# ---------------------------------------

input('..')
driver.quit()

