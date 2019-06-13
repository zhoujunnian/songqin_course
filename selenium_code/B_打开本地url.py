# coding=utf8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

#driver = webdriver.Chrome()

# 实例化一个启动参数对象
chrome_options = Options()
# 无界面运行（无窗口）
chrome_options.add_argument('--headless')
# 启动浏览器
driver = webdriver.Chrome(chrome_options=chrome_options)


# 打开本地html文件，file://
driver.get('file:///Users/zhoujunjun/PycharmProjects/PycharmData/git_hub/songqin_course/selenium_code/html/s1.html')

# 可以在查询元素的地方加一个捕捉异常，继续往下执行，不用残留页面
try:
    ele = driver.find_element_by_id("food")
    print(ele.text)
except Exception as e:
    print(e)

#-----------------获取webelement的属性-----------------------
ele = driver.find_element_by_id("baidulink")
print(ele.get_attribute('href'))

#-----------------获取webelement的stype-----------------------
ele = driver.find_element_by_id("food")
print(ele.get_attribute('style'))

#-----------------获取webelement的源码-----------------------
ele = driver.find_element_by_id("food")
print(ele.get_attribute('outerHTML'))

#-----------------获取webelement内部部分的源码-----------------------
ele = driver.find_element_by_id("food")
print(ele.get_attribute('innerHTML'))

# 对返回的字符串进行提取
foodText = ele.get_attribute('innerHTML')
ret1 = foodText.split('</span>')[1]
print(ret1)
ret2 = ret1.split('"')[1]
print(ret2)
driver.quit()

