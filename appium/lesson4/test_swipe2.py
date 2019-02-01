# coding=utf8
from appium import webdriver
import time
import traceback


desired_caps = {}
desired_caps['platformName'] = 'Android'  #测试平台
desired_caps['platformVersion'] = '7.1'   #平台版本,不能写错
desired_caps['deviceName'] = 'test'    #设备名称，多设备时需区分
# desired_caps['app'] = r'd:\apk\HiSpace.apk'  #app 文件 名，指定了要安装的app 在电脑上的路径
desired_caps['appPackage'] = 'com.huawei.appmarket'  #app package名,指定了要运行的app
desired_caps['appActivity'] = 'com.huawei.appmarket.MainActivity' #app默认Activity
desired_caps['unicodeKeyboard']  = True  # 一定要有该参数，否则unicode 输入的中文无效
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 60
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)

try:

    ele = driver.find_element_by_id('com.huawei.appmarket:id/banner')
    time.sleep(2)

    location = ele.location
    size1 = ele.size
    print(location, size1)
    x1 = location['x'] + int(size1['width'] * 0.8)
    x2 = location['x'] + int(size1['width'] * 0.2)
    y = location['y'] + int(size1['height'] * 0.5)

    for i in range(10):
        driver.swipe(start_x=x1, start_y=y, end_x=x2, end_y=y, duration=500)
        time.sleep(0.5)






except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()