# coding=utf8
from selenium import webdriver


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson02/s1.html') # 打开网址

eles = driver.find_elements_by_class_name("cheese")
for ele in eles:
    print('--------------------')
    print(ele.get_attribute('outerHTML'))

# raw_input('press any key to quit...')
driver.quit()

