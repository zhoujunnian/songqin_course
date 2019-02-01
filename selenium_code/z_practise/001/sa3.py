# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

# ------------------------
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

info = driver.find_element_by_id("forecastID")

# 再从 forecastID 元素获取所有子元素dl
html_doc = info.get_attribute('innerHTML')

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, "html5lib")

dls = soup.find_all('dl')

# 将城市和气温信息保存到列表citys中
citys = []
for dl in dls:
    name = dl.dt.a.string
    ltemp = dl.dd.find('span').string
    ltemp = int(ltemp.replace(u'℃',''))
    print(name, ltemp)
    citys.append([name,ltemp])






lowest = 100
lowestCitys = []  # 温度最低城市列表
for one in citys:
    curcity = one[0]
    ltemp = one[1]
    # 发现气温更低的城市
    if ltemp<lowest:
        lowest = ltemp
        lowestCitys = [curcity]
    #  温度和当前最低相同，加入列表
    elif ltemp ==lowest:
        lowestCitys.append(curcity)

print(u'温度最低为%s, 城市有%s' % (lowest, ','.join(lowestCitys)))

# ------------------------

driver.quit()
