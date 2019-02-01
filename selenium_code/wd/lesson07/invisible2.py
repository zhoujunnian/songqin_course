# coding:utf8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import sys

executable_path = r"d:\tools\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path)

driver.get('http://music.163.com/#/discover/toplist?id=60198')

driver.implicitly_wait(10)

# driver.switch_to.frame('g_iframe')
# div = driver.find_element_by_id("song-list-pre-cache")
# print div.text
#
# driver.switch_to.default_content()

ActionChains.move_to_element('')
div = driver.find_element_by_css_selector('div.srchbg input')
# div.send_keys('abc')
div.click()
input('...')

driver.quit()





















#
# # 抓取排行榜信息
# def getInfo():
#     driver.get('http://music.163.com/#/discover/toplist?id=60198')
#     # import time
#     # time.sleep(5)
#     # 注意下面还有一个 ID 是  auto-id-w1IbyIV6kdvzLHWE 的,那个是会变的
#     div = driver.find_element_by_id("song-list-pre-cache")
#     tbody = div.find_element_by_tag_name("tbody")
#     trList = tbody.find_element_by_tag_name('tr')
#     for tr in trList:
#         # 哪些 是有 有new 标签的 歌曲， F12 查看特性
#         newTags = tr.find_elements_by_class_name("u-icn-75")
#         if newTags:
#             print tr.text
#         else:
#             print newTags