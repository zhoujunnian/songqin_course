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
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
#driver.implicitly_wait(10)

try:
    # -----------------

    driver.find_element_by_class_name("android.widget.ImageButton")

    time.sleep(2)
    tvs = driver.find_elements_by_class_name("android.widget.TextView")
    for tv in tvs:
        print(tv.text)

    # -----------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()