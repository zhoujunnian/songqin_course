# coding=utf8

from appium import webdriver
import time,traceback



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1'  #
desired_caps['deviceName'] = 'test'
desired_caps['app'] = r'd:\apk\duoduoCalculators.apk'
desired_caps['appPackage'] = 'com.ibox.calculators' #
desired_caps['appActivity'] = 'com.ibox.calculators.SplashActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

try:
    # -----------------

    num3 = driver.find_element_by_id('com.ibox.calculators:id/digit3')
    num9 = driver.find_element_by_id('com.ibox.calculators:id/digit9')
    num5 = driver.find_element_by_id('com.ibox.calculators:id/digit5')
    plus = driver.find_element_by_id('com.ibox.calculators:id/plus')
    equal = driver.find_element_by_id('com.ibox.calculators:id/equal')
    mul  = driver.find_element_by_id('com.ibox.calculators:id/mul')

    num3.click()
    plus.click()
    num9.click()
    equal.click()
    mul.click()
    num5.click()
    equal.click()

    # ----------------------
    expression = driver.find_element_by_id('com.ibox.calculators:id/cv')
    rets = expression.find_elements_by_class_name('android.widget.TextView')
    retStr = rets[1].text

    # ----------------------


    print(retStr)
    if retStr == '60':
        print('pass')
    else:
        print('fail!')

        # -----------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()