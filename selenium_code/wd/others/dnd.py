# coding=utf-8
from selenium import webdriver
import time

executable_path = r"d:\tools\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path)

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/others/dnd.html')

# ---------------------------------------
from selenium.webdriver.common.action_chains import ActionChains

ac = ActionChains(driver)

source = driver.find_element_by_id('drag1')
print source.get_attribute('outerHTML')
target = driver.find_element_by_id('div1')
print target.get_attribute('outerHTML')

# 演示的时候，单步调试， 停在这里，再单步，可以看到效果
ac.click_and_hold(source).move_to_element(target).release().perform()



# ---------------------------------------

raw_input('..')
driver.quit()

