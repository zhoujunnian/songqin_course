# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson02/s1.html') # 打开网址


ele = driver.find_element_by_id("choose_car")
carsHtml = ele.get_attribute('innerHTML')

# 定义一个检验标准的字典
toVerify = {'volvo': '沃尔沃',
            'corolla': '卡罗拉',
            'fiat': '菲亚特',
            'audi': '奥迪'}

from bs4 import BeautifulSoup

soup = BeautifulSoup(carsHtml, "html5lib")

# 获取所有的 option 为 bs里面的 tag 对象
# 对每个tag 对象进行分析
for option in soup.find_all('option'):
    # 获取value 属性
    k = option.get('value')  # 或者 k = option['value']
    # 获取 文本内容
    v = option.get_text()  # 或者v = option.string

    print(k, v)

    if k in toVerify:
        if v != toVerify[k]:
            print('error')
        else:
            print('pass')

driver.quit()

