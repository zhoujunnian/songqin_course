# coding:utf8
import util

from selenium.webdriver.support.ui import Select


driver = util.createEasyDriver()

# 别忘了设置
driver.implicitly_wait(10)

# 抓取信息
def getInfo():
    driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

    fromEle = driver.find_element_by_id('fromStationText')
    # 为什么这里要点击一下？先没有这句话，看看什么结果
    fromEle.click()

    fromEle.clear()
    fromEle.send_keys(u'南京南\n')

    toEle = driver.find_element_by_id('toStationText')
    # 为什么这里要点击一下？先没有这句话，看看什么结果
    toEle.click()
    toEle.clear()
    toEle.send_keys(u'杭州东\n')

    # 输入开始时间，F12 看出来 是Select
    timeSelect =  Select(driver.find_element_by_id('cc_start_time'))
    timeSelect.select_by_visible_text('06:00--12:00')

    # 怎么选择明天？ f12 看看
    tomorrow = driver.find_element_by_css_selector('#date_range li:nth-child(2)')

    tomorrow.click()

    # 一点点的添加给学生看
    xpath ='//*[@id="queryLeftTable"]//td[5][@class]/../td[1]//a'

    theTrains = driver.find_elements_by_xpath(xpath)
    for one in theTrains:
        print one.text


getInfo()
