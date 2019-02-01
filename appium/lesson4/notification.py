# coding=utf8

from appium import webdriver
import time,traceback



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'test'
# desired_caps['app'] = r'e:\apk\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

try:
    # -----------------

    # raw_input('press to check notification...')
    driver.open_notifications()
    time.sleep(1)
    eles = driver.find_elements_by_xpath('//com.android.systemui.statusbar.phone.TimeAxisWidgetEx//android.widget.TextView')

    texts = []
    for ele in eles:
        t =  ele.text
        texts.append(t)


    if u'''江春阳|hello''' in '|'.join(texts):
        print 'pass'
    else:
        print 'failed'

    screenSize = driver.get_window_size()
    screenW = screenSize['width']
    screenH = screenSize['height']

    x = screenW / 2
    y1 = int(screenH * 0.8)
    y2 = int(screenH * 0.4)
    driver.swipe(start_x=x, start_y=y1, end_x=x, end_y=y2, duration=300)

    # -----------------

except:
    print traceback.format_exc()


raw_input('**** Press to quit..')
driver.quit()