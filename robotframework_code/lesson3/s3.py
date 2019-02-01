from selenium import webdriver
import time

executable_path = r"d:\tools\webdrivers\chromedriver.exe"


driver = webdriver.Chrome(executable_path)
driver.implicitly_wait(4)

# ----------------------------

driver.get('http://localhost/mgr/login/login.html')
driver.find_element_by_id("username").send_keys('auto')
driver.find_element_by_id("password").send_keys('sdfsdfsdf')


driver.find_element_by_tag_name("button").click()
time.sleep(2)

eles = driver.find_elements_by_css_selector('tr>td:nth-child(2)')

lessons = []
for ele in eles:
    lesson = ele.text
    print(lesson)
    lessons.append(lesson)



expected = ['python语言','selenium']

if lessons == expected:
    print('pass')  # 没有框架， 只能打印出来
else:
    print('fail')

# ----------------------------

driver.quit()