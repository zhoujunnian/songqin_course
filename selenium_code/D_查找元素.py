# coding=utf8
from selenium import webdriver
import selenium

driver = webdriver.Chrome(r"/Users/zhoujunjun/PycharmProjects/driver/chromedriver")
driver.get('file:///Users/zhoujunjun/PycharmProjects/PycharmData/git_hub/songqin_course/selenium_code/html/s1.html')


# ----------------by_name-------------------
try:
    ele = driver.find_element_by_name("button2")
except selenium.common.exceptions.NoSuchElementException:
    print('不存在')

# ----------------by_class-------------------
eles = driver.find_elements_by_class_name("cheese")
for ele in eles:
    print('--------------------')
    print(ele.get_attribute('outerHTML'))


eles = driver.find_elements_by_css_selector('#many >div > p.special + p')
for ele in eles:
    print(ele.get_attribute('outerHTML'))

# -----------------------------------
# css选择，class=vegetable good
eles = driver.find_elements_by_css_selector('span.vegetable.good')
for ele in eles:
    print(ele.get_attribute('outerHTML'))



# ---------------by_link--------------------

ele = driver.find_element_by_link_text("转到百度")
ele.click()

# ---------------by_partial_link--------------------

ele = driver.find_element_by_partial_link_text("百度")
ele.click()



# raw_input('press any key to quit...')
driver.quit()

