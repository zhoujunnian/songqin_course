# coding=utf-8
from selenium import webdriver
import  time


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson06/al.html')


# ----------------------------------
driver.find_element_by_id('b3').click()

time.sleep(1)

alert = driver.switch_to.alert
print(alert.text)

alert.send_keys('今天心情不错')
alert.accept()

driver.find_element_by_id('other').click()








# -------------------------------------
input('press any key to quit...')
driver.quit()   # 浏览器退出