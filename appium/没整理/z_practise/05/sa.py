# coding=utf8
from appium import webdriver
import time
import traceback


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'temp'
desired_caps['app'] = r'd:\apk\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)

try:
    # ------------------------------
    code = u'new UiSelector().resourceId("io.manong.developerdaily:id/tv_title").instance(0)'


    ele1 = driver.find_element_by_android_uiautomator(code)

    text1 = ele1.text
    print(text1)

    ele1.click()


    ele2 = driver.find_element_by_id('io.manong.developerdaily:id/tv_title')
    text2 = ele2.text

    if text1 == text2:
        print('pass')
    else:
        print('fail')

    driver.press_keycode(4)


    eles = driver.find_elements_by_id('io.manong.developerdaily:id/tab_bar_plus')

    if eles:
        print('return suscessfully')
    else:
        print('failed! cannot return')


        # ------------------------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()