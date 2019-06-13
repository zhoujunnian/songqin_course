# !/usr/bin/python开发
# -*- coding:utf-8 -*-
# Time    : 2019-03-24 12:25
# author  : Zhoujunjun
# File    : H_praticese.py
# Software: PyCharm

"""
打开百度新歌榜， http://music.baidu.com/top/new
在排名前50的歌曲中，找出其中排名上升的歌曲和演唱者
注意： 有的歌曲名里面有 "影视原声" 这样的标签， 要去掉

最终结果显示的结果如下：
我不能忘记你       :  林忆莲
等                :  严艺丹
飞天              :  云朵
粉墨              :  霍尊
春风十里不如你     :  李健
"""

# coding:utf8
from selenium import webdriver

driver = webdriver.Chrome()
# driver.implicitly_wait(1)
# 抓取排行榜信息

driver.get('http://music.baidu.com/top/new')

# 效率慢的做法
# 层层往下查找，先找有id
div = driver.find_element_by_id("songListWrapper")
# id返回的对象里面再找tag_name
ul = div.find_element_by_tag_name("ul")
# elements,加s可以查找多个li
liList = ul.find_elements_by_tag_name('li')
# 效率高，用css选择器
#liList = driver.find_elements_by_css_selector('#songListWrapper li')
for li in liList:
    # 哪些 是有 有up 标签的 歌曲， F12 查看特性
    upTags = li.find_elements_by_class_name("up")
    if upTags:

        # 由于只要 歌曲名和 演唱者名
        title = li.find_element_by_class_name("song-title")
        titleStr = title.find_element_by_tag_name("a").text

        authorsStr = li.find_element_by_class_name("author_list").text

        print('{:10s}:{}'.format(titleStr, authorsStr))

driver.quit()