# coding=utf-8
from selenium import webdriver
import time

executable_path = r"d:\tools\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path)

driver.get('https://www.vmall.com/')

# ---------------------------------------
from selenium.webdriver.common.action_chains import ActionChains

ac = ActionChains(driver)
ac.move_to_element(driver.find_element_by_id('zxnav_1')).perform()

ele= driver.find_element_by_css_selector(
    '#zxnav_1 > div.category-panels  >ul >li >a')

ele.click()


# ---------------------------------------

input('...')
driver.quit()

