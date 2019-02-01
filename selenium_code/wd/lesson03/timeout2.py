# coding:utf8
from selenium import webdriver


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)

driver.get('http://www.baidu.com')

element_keyword = driver.find_element_by_id("kw")
element_keyword.send_keys(u'松勤')

element_search_button = driver.find_element_by_id("su")
element_search_button.click()


# ================================
ele = driver.find_element_by_id('1')
print(ele.text)

if ele.text.startswith(u'松勤网 - 松勤软件测试_软件测试在线培训'):
    print('pass')
else:
    print('fail')

# ================================
driver.quit()