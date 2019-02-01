# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


executable_path = r"e:\work\sq\selenium\web_driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path) #初始化，运行chrome driver

driver.get('http://www.baidu.com') # 打开网址

loginlink = driver.find_element(By.LINK_TEXT,u"登录")
loginlink.click()

# 这次操作
username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,'TANGRAM__PSP_8__userName')))
username.click()
username.send_keys('jiangchunyang')

raw_input('press any key to quit...')
driver.quit()

