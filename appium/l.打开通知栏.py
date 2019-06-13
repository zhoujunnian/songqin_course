# coding=utf8

from appium import webdriver
import time,traceback



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
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)

try:
    # -----------------

    #time.sleep(5)
    driver.open_notifications()

    #time.sleep(1)
    # 获取通知栏所有内容
    eles = driver.find_elements_by_xpath('//android.widget.ScrollView//android.widget.TextView')

    for ele in eles:
        print(ele.text)

    time.sleep(2)

    # 收起通知栏，往上滑动
    # screenSize = driver.get_window_size()
    # screenW = screenSize['width']
    # screenH = screenSize['height']
    #
    # x = screenW / 2
    # y1 = int(screenH * 0.9)
    # y2 = int(screenH * 0.2)
    # driver.swipe(start_x=x, start_y=y1, end_x=x, end_y=y2, duration=300)


    # 按返回键收起通知栏

    driver.press_keycode(4)



    # -----------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()