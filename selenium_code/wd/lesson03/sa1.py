# coding:utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)
# 抓取排行榜信息

driver.get('http://music.baidu.com/top/new')

# 层层往下查找
div = driver.find_element_by_id("songListWrapper")
liList = div.find_elements_by_tag_name('li')

driver.implicitly_wait(0.5)
for li in liList:
    # 哪些 是有 有up 标签的 歌曲， F12 查看特性
    upTags = li.find_elements_by_class_name("up")
    if upTags:

        # 由于只要 歌曲名和 演唱者名
        title = li.find_element_by_class_name("song-title")
        titleStr = title.find_element_by_tag_name("a").text

        authorsStr = li.find_element_by_class_name("author_list").text

        print(f'{titleStr:10s}:{authorsStr}')

driver.implicitly_wait(10)

driver.quit()