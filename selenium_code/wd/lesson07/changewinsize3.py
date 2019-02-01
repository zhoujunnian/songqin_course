# coding:utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)



driver.get('http://www.12306.cn/mormhweb/')



searchbox = driver.find_element_by_css_selector(".bottom_copy a[href$='gywm/']")


searchbox.click()



input()
driver.quit()