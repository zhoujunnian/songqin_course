# coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)

def eg():
    driver.get(
        'file:///Users/zhoujunjun/PycharmProjects/PycharmData/git_hub/songqin_course/selenium_code/html/iframe.html')
    driver.switch_to.frame('baidu')
    kw = driver.find_element_by_id("kw")
    kw.send_keys(u'松勤\n')

    driver.switch_to.default_content()
    input1 = driver.find_element_by_tag_name("input")
    input1.send_keys('hello world')

    input('press any key to quit...')
    driver.quit()

def music():
    # 抓取排行榜信息
    driver.get('http://music.163.com/#/discover/toplist?id=60198')

    # --------------------------
    driver.switch_to.frame('contentFrame')
    # driver.switch_to.frame(0)
    # driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

    div = driver.find_element_by_id("song-list-pre-cache")
    print(div.text)

    # driver.switch_to.default_content()
    # ele = driver.find_element_by_id('g_nav2')
    # print(ele.text)

    driver.quit()

    #
    # # 抓取排行榜信息
    # def getInfo():
    #     driver.get('http://music.163.com/#/discover/toplist?id=60198')
    #     # import time
    #     # time.sleep(5)
    #     # 注意下面还有一个 ID 是  auto-id-w1IbyIV6kdvzLHWE 的,那个是会变的,就不要用id
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
#eg()
music()