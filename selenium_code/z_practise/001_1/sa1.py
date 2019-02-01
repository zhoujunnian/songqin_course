from selenium import webdriver
import time

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

# ------------------------
driver.get('http://121866.com/cust/sign.html')

driver.find_element_by_id("username").send_keys('gus3')
driver.find_element_by_id("password").send_keys('sdf')

driver.find_element_by_id("btn_sign").click()
time.sleep(2)

expectStr = driver.find_element_by_id("username").text
if 'gus3' ==  expectStr:
    print('测试通过')
else:
    print('测试不通过')

# ------------------------
input()
driver.quit()
