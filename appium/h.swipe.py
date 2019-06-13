# coding=utf8
from appium import webdriver
import time
import traceback


desired_capabilities = {}
desired_capabilities['platformName'] = 'Android'
desired_capabilities['automationName'] = 'Appium'
desired_capabilities['platformVersion'] = '5.1'
desired_capabilities['deviceName'] = '192.168.56.104:5555'
desired_capabilities['app'] = '/Users/zhoujunjun/Downloads/toutiao.apk'
desired_capabilities['appPackage'] = 'io.manong.developerdaily'
desired_capabilities['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_capabilities['unicodeKeyboard']  = True
desired_capabilities['noReset'] = True
desired_capabilities['newCommandTimeout'] = 6000
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities) #启动Remote RPC
#driver.implicitly_wait(10)

try:
    command = 'new UiSelector().text("我的").className("android.widget.TextView")'
    driver.find_element_by_android_uiautomator(command).click()
    ele = driver.find_element_by_id('io.manong.developerdaily:id/nav_btn_favorite')
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