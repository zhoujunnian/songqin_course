from appium import webdriver
import time
import traceback


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7'
desired_caps['deviceName'] = 'temp'
# desired_caps['app'] = r'd:\apk\HiSpace.apk'
desired_caps['appPackage'] = 'com.ibox.calculators'  #app package名,指定了要运行的app
desired_caps['appActivity'] = '.SplashActivity' #app默认Activity
desired_caps['unicodeKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)

try:
    # ------------------------------
    pass

    # ------------------------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()

