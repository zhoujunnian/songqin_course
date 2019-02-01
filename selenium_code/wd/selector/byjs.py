# coding=utf8
from selenium import webdriver


from settings import  executable_path

driver = webdriver.Chrome(executable_path) #初始化，运行chrome driver


driver.get('http://www.baidu.com') # 打开网址

kw = driver.execute_script("return $('#kw')[0]")
kw.send_keys(u'松勤\n')


print driver.name
# driver.get_screenshot_as_file('ss1.png')
# print driver.current_url
# driver.close()

raw_input('press any key to quit...')
driver.quit()

