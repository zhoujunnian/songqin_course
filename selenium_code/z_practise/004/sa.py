# coding:utf8
from selenium import webdriver
executable_path = r"d:\tools\webdrivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path)
# 别忘了设置
driver.implicitly_wait(10)

# 打开网址
driver.get('http://www.51job.com')

# --------------------------------------------

driver.find_element_by_css_selector('div.ush > a').click()


driver.find_element_by_id('kwdselectid').send_keys('python')

driver.find_element_by_id('work_position_input').click()

# 选择城市，去掉非杭州的，选择杭州
selectedCityEles = driver.find_elements_by_css_selector('#work_position_click_center em[class=on]')

for one in selectedCityEles:
    one.click()

driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()

# 保存城市选择
driver.find_element_by_id('work_position_click_bottom_save').click()


driver.find_element_by_css_selector('span.b_key').click()

driver.find_element_by_id('funtype_click').click()

driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()

driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()

driver.find_element_by_id('funtype_click_bottom_save').click()



driver.find_element_by_id('cottype_list').click()

driver.find_element_by_css_selector('#cottype_list span[data-value="01"]').click()



driver.find_element_by_id('workyear_list').click()

driver.find_element_by_css_selector('#workyear_list span[data-value="02"]').click()


driver.find_element_by_css_selector('span.p_but').click()

# 搜索结果分析
jobs = driver.find_elements_by_css_selector('#resultList div[class=el]')
for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    stringFilelds = [field.text for field in fields]
    print(' | '.join(stringFilelds))

# --------------------------------------------

driver.quit()