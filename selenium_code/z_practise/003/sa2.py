# coding:utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)


driver.get('http://www.51job.com')

driver.find_element_by_id('kwdselectid').send_keys('python')
driver.find_element_by_id('work_position_input').click()


# 选择城市，去掉非杭州的，选择杭州
selectedCityEles = driver.find_elements_by_css_selector('#work_position_click_center em[class=on]')

for one in selectedCityEles:
    one.click()

driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()

# 保存城市选择
driver.find_element_by_id('work_position_click_bottom_save').click()
driver.find_element_by_css_selector('div.ush > button').click()

# 搜索结果分析
jobs = driver.find_elements_by_css_selector('#resultList div[class=el]')
for job in jobs:

    fields = job.find_elements_by_tag_name('span')
    stringFilelds = [field.text for field in fields]
    print(' | '.join(stringFilelds))

driver.quit()