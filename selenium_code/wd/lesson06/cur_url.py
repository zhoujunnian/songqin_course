# coding:utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)


driver.get('https://www.baidu.com/')
print(driver.title)
print(driver.current_url)

driver.find_element_by_id("kw").send_keys(u'松勤\n')
driver.find_element_by_id('1')
print(driver.title)
print(driver.current_url)

driver.quit()