# coding=utf8
from selenium import webdriver


from settings import  executable_path

driver = webdriver.Chrome(executable_path) #初始化，运行chrome driver


driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/selector/s1.html')

ele = driver.execute_script("return $('#food')[0]")

print ele.text

raw_input('press any key to quit...')
driver.quit()

