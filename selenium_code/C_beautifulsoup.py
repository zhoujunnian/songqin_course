"""
具体使用看：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
"""

# 获取html内容字符串，进行分析
with open('/Users/zhoujunjun/PycharmProjects/PycharmData/git_hub/songqin_course/selenium_code/html/s1.html',encoding='utf8') as f:
    html_doc = f.read()

# 导入 BeautifulSoup
from bs4 import BeautifulSoup
from selenium import webdriver

# 指定用html5lib来解析html文档
soup = BeautifulSoup(html_doc, "html5lib")
print(soup.button.string)

tag = soup.find('select',id="choose_car")
print(tag)



driver = webdriver.Chrome(r"/Users/zhoujunjun/PycharmProjects/driver/chromedriver")
driver.get('file:///Users/zhoujunjun/PycharmProjects/PycharmData/git_hub/songqin_course/selenium_code/html/s1.html')
ele = driver.find_element_by_id("choose_car")
carsHtml = ele.get_attribute('innerHTML')
print(carsHtml)

# 定义一个检验标准的字典
toVerify = {'volvo': '沃尔沃',
            'corolla': '卡罗拉',
            'fiat': '菲亚特',
            'audi': '奥迪'}

# 获取所有的 option 为 bs里面的 tag 对象
# 对每个tag 对象进行分析
for option in soup.find_all('option'):
    # 获取value 属性
    k = option.get('value')  # 或者 k = option['value']
    # 获取 文本内容
    v = option.get_text()  # 或者v = option.字符串格式化

    print(k, v)

    if k in toVerify:
        if v != toVerify[k]:
            print('error')
        else:
            print('pass')

driver.quit()