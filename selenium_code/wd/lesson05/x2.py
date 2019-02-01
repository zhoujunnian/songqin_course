# coding=utf8
from selenium import webdriver

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson05/xpath.html')



ele = driver.find_element_by_xpath("//*[@id='pork']/..")
print (ele.text.split('#')[1])

# eles = driver.find_elements_by_xpath("//*[@id='beef']/../..//span[@price>20]")
# for ele in eles:
#     print(ele.text)

driver.quit()

