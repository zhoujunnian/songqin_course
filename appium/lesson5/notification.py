# coding=utf8

from appium import webdriver
import time,traceback



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7'
desired_caps['deviceName'] = 'test'
# desired_caps['app'] = r'd:\apk\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

try:
    # -----------------

    time.sleep(5)
    driver.open_notifications()

    time.sleep(1)
    eles = driver.find_elements_by_xpath('//android.widget.ScrollView//android.widget.TextView')

    for ele in eles:
        print(ele.text)

    time.sleep(2)
    # screenSize = driver.get_window_size()
    # screenW = screenSize['width']
    # screenH = screenSize['height']
    #
    # x = screenW / 2
    # y1 = int(screenH * 0.9)
    # y2 = int(screenH * 0.2)
    # driver.swipe(start_x=x, start_y=y1, end_x=x, end_y=y2, duration=300)



    driver.press_keycode(4)



    # -----------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()