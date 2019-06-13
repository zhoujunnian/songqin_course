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

try:

    # ------------------------------

    command = 'new UiSelector().text("我的").className("android.widget.TextView")'
    driver.find_element_by_android_uiautomator(command).click()

    # 找到这个元素，后面再执行，避免页面还没加载出来
    ele1 = driver.find_element_by_id('io.manong.developerdaily:id/nav_btn_favorite')

    screenSize = driver.get_window_size()
    screenW = screenSize['width']
    screenH = screenSize['height']

    x = screenW / 2
    y1 = int(screenH * 0.8)
    y2 = int(screenH * 0.4)
    driver.swipe(x, y1, x, y2, 500)

    driver.find_element_by_id('io.manong.developerdaily:id/nav_btn_setting').click()








    # ------------------------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()