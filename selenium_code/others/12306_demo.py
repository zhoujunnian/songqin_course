# -*- coding: utf-8 -*-
from selenium import webdriver
import time

# 初始化，运行chrome driver，打开浏览器
driver = webdriver.Chrome()

# 设置浏览窗口大小
driver.set_window_size(1080,900)

# 设置全局操作超时时间
driver.implicitly_wait(10)

# 打开网址
driver.get('https://kyfw.12306.cn')

# # 登录
# driver.find_element_by_id("login_user").click()
# driver.find_element_by_id("username").send_keys('pppoe4444')
# driver.find_element_by_id("password").send_keys('xxxx')
# raw_input(u"请填写验证码图片,完成后继续。。。")

driver.find_element_by_link_text(u"车票预订").click()


# 出发地选择
driver.find_element_by_id("fromStationText").click()
driver.find_element_by_css_selector(u"[title=杭州]").click()


# 到达地选择
driver.find_element_by_id("toStationText").click()
driver.find_element_by_css_selector(u"[title=南京]").click()


# 出发日期选择
driver.find_element_by_id("train_date").click()
driver.find_element_by_css_selector(
'body > div.cal-wrap > div:nth-child(1) > div.cal-cm > div:nth-child(22) > div').click()


# 勾选 车次类型 为高铁
driver.find_element_by_css_selector("#_ul_station_train_code>li:first-child").click()


while True:
    try:
        # 点击 查询 按钮
        driver.find_element_by_id("query_ticket").click()

        ele = driver.find_element_by_id("ZE_56000G431400")
        ele.click()

        if ele.text  in  [u'无','--']:
            print('暂时无票，继续查询')
            time.sleep(1)
        else:
            print('有票，购买')
    except:
        pass




raw_input('press to exit')
driver.quit()   # 浏览器退出
