from appium import webdriver
 
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
print(driver.session_id)

# 等待界面出现
driver.find_element_by_class_name("android.widget.ImageButton")
# 点击 右下角 我的
driver.tap([(640,1250)],300)

input('**** Press to quit..')
driver.quit()