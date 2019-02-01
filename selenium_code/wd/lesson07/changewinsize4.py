# coding:utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)



driver.get('http://music.163.com')


# 结果像这样 {'width': 855, 'height': 922}
size = driver.get_window_size()
# 只改变宽带
driver.set_window_size(1400, size['height'])



searchbox = driver.find_element_by_css_selector('#g_search input')


searchbox.send_keys('张学友\n')




driver.quit()