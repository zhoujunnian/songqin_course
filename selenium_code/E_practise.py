"""
task1:
1. 访问天气查询网站（网址如下），查询江苏省天气
http://www.weather.com.cn/html/province/jiangsu.shtml
2. 获取江苏所有城市的天气，并找出其中每天最低气温最低的城市，显示出来，比如
温度最低为12℃, 城市有连云港 盐城

"""
from selenium import webdriver
driver = webdriver.Chrome()

# 方法1
def method1():
    # ------------------------
    driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

    ele = driver.find_element_by_id("forecastID")
    print(ele.text)

    ''' 
    citysWeather是每个城市的温度信息 list
    
    每个元素像这样：
    南京
    12℃/27
    '''
    citysWeather = ele.text.split(u'℃\n')
    print(citysWeather)

    # 算出温度最低城市

    lowest = 100
    lowestCity = []  # 温度最低城市列表
    for one in citysWeather:
        one = one.replace(u'℃','')
        print(one)
        curcity = one.split('\n')[0]
        lowweather = one.split('/')[1]
        lowweather = int(lowweather)
        # 发现气温更低的城市
        if lowweather<lowest:
            lowest = lowweather
            lowestCity = [curcity]
        #  温度和当前最低相同，加入列表
        elif lowweather ==lowest:
            lowestCity.append(curcity)

    print('温度最低为%s℃, 城市有%s' % (lowest, ' '.join(lowestCity)))

    # ------------------------

    driver.quit()



# 方法2
def method2():

    driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

    ele = driver.find_element_by_id("forecastID")
    print(ele.text)


    # 再从 forecastID 元素获取所有子元素dl
    dls = ele.find_elements_by_tag_name('dl')

    # 将城市和气温信息保存到列表citys中
    citys = []
    for dl in dls:
        # print dl.get_attribute('innerHTML')

        name = dl.find_element_by_tag_name('dt').text
        # 最高最低气温位置会变，根据位置决定是span还是b
        ltemp = dl.find_element_by_tag_name('span').text

        ltemp = int(ltemp.replace('℃',''))
        print(name, ltemp)
        citys.append([name, ltemp])

    lowest = None
    lowestCitys = []  # 温度最低城市列表
    for one in citys:
        curcity = one[0]
        ltemp = one[1]
        # 发现气温更低的城市
        if lowest==None or ltemp<lowest:
            lowest = ltemp
            lowestCitys = [curcity]
        #  温度和当前最低相同，加入列表
        elif ltemp ==lowest:
            lowestCitys.append(curcity)

    print('温度最低为%s℃, 城市有%s' % (lowest, ' '.join(lowestCitys)))



# 方法3
def method3():

    driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

    ele = driver.find_element_by_id("forecastID")

    # -----------------------------------
    # 再用bs4分析
    html_doc = ele.get_attribute('innerHTML')

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_doc, "html5lib")

    # 发现每个城市的信息都在dl里面
    dls = soup.find_all('dl')

    # 将城市和气温信息保存到列表citys中
    citys = []
    for dl in dls:
        name = dl.dt.a.string
        ltemp = dl.dd.span.string
        ltemp = int(ltemp.replace('℃',''))
        print(name, ltemp)
        citys.append([name,ltemp])


    lowest = None
    lowestCitys = []  # 温度最低城市列表
    for one in citys:
        curcity = one[0]
        ltemp = one[1]
        # 发现气温更低的城市
        if lowest==None or ltemp<lowest:
            lowest = ltemp
            lowestCitys = [curcity]
        #  温度和当前最低相同，加入列表
        elif ltemp ==lowest:
            lowestCitys.append(curcity)

    print('温度最低为%s℃, 城市有%s' % (lowest, ' '.join(lowestCitys)))

method2()