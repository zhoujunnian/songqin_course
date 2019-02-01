# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

# 打开网址
driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson04/cb.html')

input1 = driver.find_element(By.CSS_SELECTOR,"input[value=car]")
# 判断 是否已经选中
selected = input1.is_selected()
if selected:
    print('car already selected')
else:
    print('car not selected, click on it ')
    input1.click()



input('press any key to quit...')
driver.quit()   # 浏览器退出