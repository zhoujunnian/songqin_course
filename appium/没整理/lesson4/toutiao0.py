# coding=utf8

from appium import webdriver
import time,traceback



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7'
desired_caps['deviceName'] = 'temp'
desired_caps['app'] = r'd:\apk\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

try:
    code = 'new UiSelector().text("我的").className("android.widget.TextView")'
    ele = driver.find_element_by_android_uiautomator(code)

    ele.click()

    # -----------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()