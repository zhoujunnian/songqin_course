# coding:utf8
from selenium import webdriver

# 导入浏览器驱动路径
executable_path = r"d:\tools\webdrivers\chromedriver.exe"


# 指定是chrome 的驱动
# 执行到这里的时候Selenium会去到指定的路径将chrome driver 程序运行起来

driver = webdriver.Chrome(executable_path)

# ------------------------

driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

# 分析html发现 温度信息在forecastID 子元素dl里面
info = driver.find_element_by_id("forecastID")

# 再从 forecastID 元素获取所有子元素dl
dls = info.find_elements_by_tag_name('dl')

# 将城市和气温信息保存到列表citys中
citys = []
for dl in dls:
    # print dl.get_attribute('innerHTML')

    name = dl.find_element_by_tag_name('dt').text
    # 最高最低气温位置会变，根据位置决定是span还是b
    ltemp = dl.find_element_by_tag_name('b').text

    ltemp = int(ltemp.replace(u'℃',''))
    print(name, ltemp)
    citys.append([name, ltemp])

lowest = 100
lowestCitys = []  # 温度最低城市列表
for one in citys:
    curcity = one[0]
    ltemp = one[1]
    curlowweather = ltemp
    # 发现气温更低的城市
    if curlowweather<lowest:
        lowest = curlowweather
        lowestCitys = [curcity]
    #  温度和当前最低相同，加入列表
    elif curlowweather ==lowest:
        lowestCitys.append(curcity)

print('温度最低为%s, 城市有%s' % (lowest, ','.join(lowestCitys)))

# ------------------------
driver.quit()