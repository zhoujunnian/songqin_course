# coding:utf8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.ui import Select

executable_path = r"d:\tools\webdrivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path)
driver.implicitly_wait(10)

# 抓取信息
def getInfo():
    driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

    fromEle = driver.find_element_by_id('fromStationText')
    fromEle.click()
    fromEle.clear()
    fromEle.send_keys(u'南京南\n')


    toEle = driver.find_element_by_id('toStationText')
    fromEle.click()
    toEle.clear()
    toEle.send_keys(u'杭州东\n')


    Select(driver.find_element_by_id('cc_start_time'))\
        .select_by_visible_text('06:00--12:00')

    driver.find_element_by_css_selector('#date_range > ul >li:nth-child(2)').click()

    # xpath = "//*[@id='queryLeftTable']/tr/td[4][@class]/../td[1]//a"
    # eles = driver.find_elements_by_xpath(xpath)
    # for one in eles:
    #     print one.text

    driver.find_element_by_id('queryLeftTable')
    time.sleep(1)
    ele = driver.find_element_by_id('queryLeftTable')
    print(ele.get_attribute('innerHTML'))


getInfo()

driver.quit()