# -*- coding: utf-8 -*-
from selenium import webdriver


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson04/input1.html') # 打开网址


input1 = driver.find_element_by_id("input1")
input1.clear()
input1.send_keys('输入我想输入的字符222')
print(input1.get_attribute('value'))

# ta1 = driver.find_element_by_id("ta1")
# ta1.send_keys(u'春眠不觉晓\n处处闻啼鸟')



input('press any key to quit...')
driver.quit()