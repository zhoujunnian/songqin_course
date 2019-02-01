# coding=utf8
from appium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import traceback
 
desired_caps = {}
desired_caps['platformName'] = 'Android'  #测试平台
desired_caps['platformVersion'] = '7.1'   #平台版本,不能写错
desired_caps['deviceName'] = 'test'    #设备名称，多设备时需区分
# desired_caps['app'] = 'e:\\toutiao.apk'  #app package名
desired_caps['appPackage'] = 'io.manong.developerdaily'  #app package名
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity' #app默认Activity
desired_caps['unicodeKeyboard']  = True  # 一定要有该参数，否则unicode 输入的中文无效
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)


try:

    # ------------------------------

    command = 'new UiSelector().text("我的").className("android.widget.TextView")'
    driver.find_element_by_android_uiautomator(command).click()

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