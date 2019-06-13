# coding=utf8
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import traceback
 
desired_caps = {}
desired_caps['platformName'] = 'Android'  #测试平台
desired_caps['platformVersion'] = '7'   #平台版本,不能写错
desired_caps['deviceName'] = 'temp'    #设备名称，多设备时需区分
desired_caps['app'] = r'd:\apk\wv.apk'  #app 文件 名，指定了要安装的app 在电脑上的路径
desired_caps['appPackage'] = 'com.example.jcy.wvtest'  #app package名,指定了要运行的app
desired_caps['appActivity'] = '.MainActivity' #app默认Activity
desired_caps['unicodeKeyboard']  = True  # 一定要有该参数，否则unicode 输入的中文无效
desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)

try:
    # -----------------
    driver.find_element_by_accessibility_id('unique name').send_keys(u'关羽')

    # -----------------


except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()