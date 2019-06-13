from selenium import webdriver


# 指定是chrome 的驱动
# 执行到这里的时候Selenium会去到指定的路径将chrome driver 程序运行起来

driver = webdriver.Chrome(r"/Users/zhoujunjun/PycharmProjects/driver/chromedriver")

# get 方法 打开指定网址
driver.get('http://www.baidu.com')
print(driver.get_cookies())

# 查找到那个搜索输入栏网页元素，返回一个表示该元素的WebElement对象。
element_keyword = driver.find_element_by_id("kw")

# 输入字符
element_keyword.send_keys('松勤')

# 找到搜索按钮
element_search_button = driver.find_element_by_id("su")
# 点击该元素
element_search_button.click()


# ================================
import time
time.sleep(2)
ret = driver.find_element_by_id('1')
print(ret.text)     # text属性，表示页面显示的内容

if ret.text.startswith('松勤网 - 松勤软件测试'):
    print('测试通过')
else:
    print('测试不通过')

# ================================
input()     # 输入字符，执行pass，继续往下执行

# 最后，driver.quit让浏览器和驱动进程一起退出。不然会有好几个实例一起运行

driver.quit()