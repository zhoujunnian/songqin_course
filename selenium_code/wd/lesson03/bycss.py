# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson03/s1.html')


eles = driver.find_elements_by_css_selector('#choose_car option')

for ele in eles:
    print(ele.get_attribute('outerHTML'))

# raw_input('press any key to quit...')
driver.quit()

