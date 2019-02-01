# coding:utf8
from selenium import webdriver
executable_path = r"d:\tools\webdrivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path)
# 别忘了设置
driver.implicitly_wait(10)

# 打开网址
driver.get('http://www.51job.com')

# 选择高级搜索 ， 可以用 a[href*=advance_search]  也可以用 div.ush > a
driver.find_element_by_css_selector('div.ush > a').click()


# 输入选择关键词
driver.find_element_by_id('kwdselectid').send_keys('python')

# 工作地点选择
driver.find_element_by_id('work_position_input').click()

# 取消 已经选择的
selectedCityEles = driver.find_elements_by_css_selector('#work_position_click_center em[class=on]')



for one in selectedCityEles:
    one.click()



import traceback
for one in selectedCityEles:
    try:
        one.click()
    except:
        print(traceback.format_exc())
        input('出现问题，看看界面')


# 选杭州
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()

# 保存选择
driver.find_element_by_id('work_position_click_bottom_save').click()


# 要点一下别的地方， 否则下面的元素会被挡住，先不加下面的代码，给大家看看有什么问题
driver.find_element_by_css_selector('div.tit').click()



# 职能类别 选 计算机软件 -> 高级软件工程师

driver.find_element_by_id('funtype_click').click()


driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()

driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()


driver.find_element_by_id('funtype_click_bottom_save').click()

# 公司性质选 外资 欧美
driver.find_element_by_id('cottype_list').click()
driver.find_element_by_css_selector('#cottype_list span.li[data-value="01"]').click()

# 工作年限选
driver.find_element_by_id('workyear_list').click()
driver.find_element_by_css_selector('#workyear_list span.li[data-value="02"]').click()

# 点击搜索
driver.find_element_by_css_selector('div.p_sou > span.p_but').click()

# 结果列表获取内容
jobs = driver.find_elements_by_css_selector('#resultList div[class=el]')


for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    stringFilelds = [field.text for field in fields]
    print(' | '.join(stringFilelds))

driver.quit()