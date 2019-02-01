# coding:utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)


driver.get('https://www.baidu.com/')
print(driver.title)

driver.find_element_by_id("kw").send_keys('松勤\n')

print(driver.title)

driver.quit()