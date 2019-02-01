from selenium import webdriver
import time

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

# ------------------------
driver.get('http://121866.com/cust/sign.html')
driver.implicitly_wait(10)

driver.find_element_by_id("username").send_keys('gus')
driver.find_element_by_id("password").send_keys('sdf')

driver.find_element_by_id("btn_sign").click()


ele = driver.find_element_by_css_selector(".list-item")
print(f'管理界面的网页标题是：{ele.text}')
ele.click()

import time
time.sleep(2)
# 注意这个是div.title是二次渲染后才得到的值
ele = driver.find_element_by_css_selector("div.title")
print(f'打开网页后，标题是：{ele.text}')

# ------------------------
input()
driver.quit()
