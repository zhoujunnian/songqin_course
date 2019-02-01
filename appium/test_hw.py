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
desired_caps['platformVersion'] = '6.0'   #平台版本,不能写错
desired_caps['deviceName'] = 'test'    #设备名称，多设备时需区分
desired_caps['app'] = r'e:\apk\HiSpace.apk'  #app 文件 名，
desired_caps['appPackage'] = 'com.huawei.appmarket'  #app package名,指定了要运行的app
desired_caps['appActivity'] = 'com.huawei.appmarket.MainActivity' #app默认Activity
desired_caps['unicodeKeyboard']  = True  # 一定要有该参数，否则unicode 输入的中文无效
desired_caps['resetKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC

try:
    print 1
    driver.implicitly_wait(10)

    print driver.app_strings
    xpath = u'//*[@resource-id="com.huawei.appmarket:id/tabLayout"]//android.widget.TextView[last()]'
    ele = driver.find_element_by_xpath(xpath)
    print ele.text


    # print driver.current_activity
    # driver.press_keycode(4)  # 按返回键
    # time.sleep(1)
    # print driver.current_activity

except:
    print traceback.format_exc()


raw_input('**** Press to quit..')
driver.quit()