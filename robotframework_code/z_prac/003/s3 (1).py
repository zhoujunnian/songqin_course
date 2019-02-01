# coding:utf8
from selenium import webdriver

executable_path = r"d:\tools\webdrivers\chromedriver.exe"


driver = webdriver.Chrome(executable_path)
driver.implicitly_wait(4)

# ----------------------------
driver.get('https://www.vmall.com/')

eles = driver.find_elements_by_css_selector('.home-hot-goods .grid-items:not(.grid-items-sm) h3')

lessons = []
for ele in eles:
    print ele.get_attribute('innerText')
    print '----------------'
    print ele.text

# ----------------------------

driver.quit()

#