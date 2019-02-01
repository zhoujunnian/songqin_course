from selenium import webdriver
driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

# ------------------------
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

ele = driver.find_element_by_id("forecastID")
print(ele.text)

# 写到这里，先运行一下，看看执行结果
# 然后就是安装我们前面的一贯的思路，可以将
# 每个城市的信息存放到一个列表中
# 问大家怎么做？


citysWeather = ele.text.split(u'℃\n')

# 这样：citysWeather是每个城市的温度信息 list
#
# 每个元素像这样：
# 南京
# 12℃/27


#下面就是算法，算出温度最低城市，
# 有很多方法，大家看看这种

# 我们循环 去遍历这个城市文档信息列表，
# 得到城市名和 低气温的值，
#
# 依次和取出当前的所有城市最低气温比较，
# 如果更低，就记录到当前的低温城市列表中。


lowest = None  #  记录目前最低温，先设置为None
lowestCitys = []  # 温度最低城市列表
for one in citysWeather:
    one = one.replace('℃','')
    print(one)
    curcity = one.split('\n')[0]
    lowweather = one.split('/')[1]
    lowweather = int(lowweather)
    # 还没有最低温记录，或者发现气温更低的城市
    # 注意 条件不能写反
    if lowest==None or lowweather<lowest:
        lowest = lowweather
        lowestCity = [curcity]
    #  温度和当前最低相同，加入列表
    elif lowweather ==lowest:
        lowestCity.append(curcity)

print('温度最低为%s℃, 城市有%s' % (lowest, ' '.join(lowestCity)))

# ------------------------

driver.quit()