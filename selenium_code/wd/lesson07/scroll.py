# coding:utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)



driver.get('http://music.163.com')

driver.execute_script('window.scrollBy(1000,0)')

searchbox = driver.find_element_by_css_selector('#g_search input')


searchbox.send_keys('张学友\n')




driver.quit()