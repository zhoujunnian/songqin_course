# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson02/s1.html') # 打开网址



from selenium.common.exceptions import NoSuchElementException

ele = driver.find_element_by_id("food")

print(ele.get_attribute('innerHTML'))

driver.quit()

