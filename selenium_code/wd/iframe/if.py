# coding=utf-8
from selenium import webdriver

executable_path = r"e:\work\sq\selenium\web_driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path)

driver.get('file:///E:/work/sq/selenium/samples_selenium/wd/iframe/if.html')

driver.switch_to.frame('baidu')
kw = driver.find_element_by_id("kw")
kw.send_keys(u'松勤\n')

driver.switch_to.default_content()
input1 = driver.find_element_by_tag_name("input")
input1.send_keys('hello world')

raw_input('press any key to quit...')
driver.quit()