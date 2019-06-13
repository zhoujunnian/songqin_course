# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"/Users/zhoujunjun/PycharmProjects/driver/chromedriver")
driver.get('file:///Users/zhoujunjun/PycharmProjects/PycharmData/git_hub/songqin_course/selenium_code/html/s1.html')


input1 = driver.find_element_by_id("input1")
input1.clear()
input1.send_keys('输入我想输入的字符222')
# 获取输入框内容
print(input1.get_attribute('value'))

# 单选
# 这里使用了根据属性值来查找
input1 = driver.find_element_by_css_selector("input[value=female]")
input1.click()

# 勾选框
input2 = driver.find_element(By.CSS_SELECTOR,"input[value=car]")
# 判断 是否已经选中
selected = input2.is_selected()
if selected:
    print('car already selected')
else:
    print('car not selected, click on it ')
    input2.click()


# 复选框
# 导入 Select
from selenium.webdriver.support.ui import Select
# 获得相应的WebElement
select = Select(driver.find_element_by_id("multi"))
# 先去掉选择所有的 选项
select.deselect_all()
# 选择对应的
select.select_by_visible_text("雅阁")
select.select_by_visible_text("宝马 740")


# 获得相应的WebElement
select = Select(driver.find_element_by_id("single"))
select.select_by_visible_text("男")
#select.select_by_visible_text("女")

input('press any key to quit...')
#driver.quit()