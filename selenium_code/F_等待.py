# coding:utf8
from selenium import webdriver

driver = webdriver.Chrome()

# 隐式等待
driver.implicitly_wait(3)

driver.get('http://www.baidu.com')
element_keyword = driver.find_element_by_id("kw")
element_keyword.send_keys(u'松勤')
element_search_button = driver.find_element_by_id("su")
element_search_button.click()


# 显式等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
ele = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID,'1')))

print(ele.text)

if ele.text.startswith(u'松勤网 - 松勤软件测试_软件测试在线培训'):
    print('pass')
else:
    print('fail')

# ================================
driver.quit()