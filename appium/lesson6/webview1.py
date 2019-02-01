# coding=utf8
from appium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import traceback
 
desired_caps = {}
desired_caps['platformName'] = 'Android'  #测试平台
desired_caps['platformVersion'] = '7'   #平台版本,不能写错
desired_caps['deviceName'] = 'test'    #设备名称，多设备时需区分
# desired_caps['app'] = r'd:\apk\wv.apk'  #app package名
desired_caps['appPackage'] = 'com.example.jcy.wvtest'  #app package名
desired_caps['appActivity'] = '.MainActivity' #app默认Activity
desired_caps['unicodeKeyboard']  = True
desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC

driver.implicitly_wait(10)
try:
    # -----------------------


    time.sleep(3)
    print(driver.contexts)
    print(driver.current_context)

    driver.switch_to.context('WEBVIEW_com.example.jcy.wvtest')

    driver.find_element_by_id('index-kw').send_keys('松勤')

    driver.find_element_by_id('index-bn').click()

    driver.switch_to.context('NATIVE_APP')
    driver.find_element_by_id('com.example.jcy.wvtest:id/navigation_dashboard').click()
    time.sleep(2)
    driver.find_element_by_id('com.example.jcy.wvtest:id/navigation_notifications').click()


    # -----------------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()