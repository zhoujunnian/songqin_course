# !/usr/bin/python开发
# -*- coding:utf-8 -*-
# Time    : 2019-03-24 14:26
# author  : Zhoujunjun
# File    : I_practise.py
# Software: PyCharm

"""
登录 51job ，
http://www.51job.com

输入搜索关键词 "python开发"， 地区选择 "杭州"（注意，如果所在地已经选中其他地区，要去掉），
搜索最新发布的职位， 抓取页面信息。 得到如下的格式化信息

Python开发工程师 | 杭州纳帕科技有限公司 | 杭州 | 0.8-1.6万/月 | 04-27
Python高级开发工程师 | 中浙信科技咨询有限公司 | 杭州 | 1-1.5万/月 | 04-27
高级Python开发工程师 | 杭州新思维计算机有限公司 | 杭州-西湖区 | 1-1.5万/月 | 04-27

"""
# 方法一
# coding:utf8
from selenium import webdriver
import time
driver = webdriver.Chrome()
# 别忘了设置
driver.implicitly_wait(10)

# 抓取信息
driver.get('http://www.51job.com')

driver.find_element_by_id('kwdselectid').send_keys('python开发')
# 点击工作地点
driver.find_element_by_id('work_position_input').click()

# 最近网站更新了，好像前端处理有滞后，需要sleep 一下
time.sleep(2)

# 选择所有城市，去掉非杭州的且选择杭州，
# 如果是杭州但是没有选，选上这些城市
cityEles = driver.find_elements_by_css_selector('#work_position_click_center_right em')

for one in cityEles:
    cityName = one.text
    selected = one.get_attribute('class')
    # print cityName,seleted

    if cityName == u'杭州':
        if selected != 'on':
            one.click()

    else:
        if selected == 'on':
            one.click()

# 保存城市选择
driver.find_element_by_id('work_position_click_bottom_save').click()

# 点击搜索
driver.find_element_by_css_selector('.ush  button').click()

# 搜索结果分析
jobs = driver.find_elements_by_css_selector('#resultList  div.el')

for job in jobs:
    # 去掉第一行：标题行
    if 'title' in job.get_attribute('class'):
        continue

    filelds = job.find_elements_by_tag_name('span')
    strField = [fileld.text for fileld in filelds]
    print(' | '.join(strField))

driver.quit()


# 方法二
# coding:utf8
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('http://www.51job.com')

driver.find_element_by_id('kwdselectid').send_keys('python开发')
driver.find_element_by_id('work_position_input').click()

# 选择城市，去掉非杭州的，选择杭州
selectedCityEles = driver.find_elements_by_css_selector(
    '#work_position_click_center_right_list_000000 em[class=on]')

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

#driver.quit()