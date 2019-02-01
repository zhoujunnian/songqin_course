# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

executable_path = r"e:\work\sq\selenium\web_driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path)

driver.get('http://www.baidu.com') # 打开网址

loginlink = driver.find_element(By.LINK_TEXT,u"登录")
loginlink.click()

#以后的选择元素操作最多等待10秒
driver.implicitly_wait(10) # seconds
username = driver.find_element(By.ID,'TANGRAM__PSP_8__userName')
username.click()
username.send_keys('jiangchunyang')

raw_input('press any key to quit...')
driver.quit()

