# coding=utf8
from appium import webdriver
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
#driver.implicitly_wait(10)


try:

    # ------------------------------

    command = 'new UiSelector().text("我的").className("android.widget.TextView")'
    driver.find_element_by_android_uiautomator(command).click()

    ele1 = driver.find_element_by_id('io.manong.developerdaily:id/nav_btn_favorite')
    driver.swipe(start_x=300, start_y=1000, end_x=300, end_y=500, duration=500)
    driver.find_element_by_id('io.manong.developerdaily:id/nav_btn_setting').click()

    # ------------------------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()