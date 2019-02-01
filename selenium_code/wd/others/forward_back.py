# coding=utf-8
from selenium import webdriver
import  time


executable_path = r"d:\tools\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path)



# ----------------------------------

# ----------------------------------
raw_input('press any key to quit...')
driver.quit()   # 浏览器退出