from selenium import  webdriver
import time

from selenium.webdriver.support.ui  import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)


driver.get('https://kyfw.12306.cn/otn/leftTicket/init')

fromStation = driver.find_element_by_id('fromStationText')
fromStation.click()
fromStation.clear()
fromStation.send_keys('南京南\n')


toStation = driver.find_element_by_id('toStationText')
toStation.click()
toStation.clear()
toStation.send_keys('杭州东\n')

timeEle = Select( driver.find_element_by_id('cc_start_time'))
timeEle.select_by_visible_text('06:00--12:00')

driver.find_element_by_css_selector('#date_range>ul>li:nth-child(2)').click()


# 判断是否有查询超时的错误
while True:

    time.sleep(2)
    print('before find ..')
    eles = driver.find_elements_by_css_selector('#queryLeftTable tr')

    print('after find ..')

    if not eles:
        print('not found ')
        driver.find_element_by_id('query_ticket').click()
    else:
        break



xpath ='//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'

theTrains = driver.find_elements_by_xpath(xpath)
for one in theTrains:
    print (one.text)



#driver.quit()
