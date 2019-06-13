# coding=utf8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
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

try:
    print(1)
    #driver.implicitly_wait(10)

    print(driver.app_strings)
    xpath = u'//*[@resource-id="com.huawei.appmarket:id/tabLayout"]//android.widget.TextView[last()]'
    ele = driver.find_element_by_xpath(xpath)
    print(ele.text)


    # print driver.current_activity
    # driver.press_keycode(4)  # 按返回键
    # time.sleep(1)
    # print driver.current_activity

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()