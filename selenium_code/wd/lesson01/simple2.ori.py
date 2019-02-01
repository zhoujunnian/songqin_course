from selenium import webdriver



# 指定是chrome 的驱动
# 执行到这里的时候Selenium会去到指定的路径将chrome driver 程序运行起来

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

# get 方法 打开指定网址
driver.get('http://www.baidu.com')

# 查找到那个搜索输入栏网页元素，返回一个表示该元素的WebElement对象。
element_keyword = driver.find_element_by_id("kw")


element_keyword.send_keys(u'松勤')  # 输入字符

# 找到搜索按钮
element_search_button = driver.find_element_by_id("su")
# 点击该元素
element_search_button.click()


# ================================

# ================================

driver.quit()