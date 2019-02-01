# coding:utf8
from selenium import webdriver
executable_path = r"d:\tools\webdrivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path)
driver.implicitly_wait(10)


driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson07/winsize.html')

searchbox = driver.find_element_by_tag_name('input')

searchbox.send_keys('你好啊\n')


input('...')
driver.quit()