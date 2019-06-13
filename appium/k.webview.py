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
    # -----------------------


    time.sleep(3)
    print(driver.contexts)
    print(driver.current_context)
    # 切换到webview，在webview进行自动化（app里面的网页自动化）
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