from appium import webdriver
 
desired_caps = {}
desired_caps['platformName'] = 'Android'  #测试平台
desired_caps['platformVersion'] = '7.1'   #平台版本,不能写错
desired_caps['deviceName'] = 'test'    #设备名称，多设备时需区分
# desired_caps['app'] = r'd:\apk\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'  #app package名
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity' #app默认Activity
desired_caps['unicodeKeyboard']  = True  # 一定要有该参数，否则unicode 输入的中文无效
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)
print(driver.session_id)

# 等待界面出现
driver.find_element_by_class_name("android.widget.ImageButton")
# 点击 右下角 我的
driver.tap([(640,1250)],300)

input('**** Press to quit..')
driver.quit()