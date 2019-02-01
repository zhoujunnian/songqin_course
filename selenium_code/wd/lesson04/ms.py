# coding=utf-8
from selenium import webdriver


driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")

driver.get('file:///D:/gsync/workspace/sq/selenium/samples_selenium/wd/lesson04/ms.html') # 打开网址


# 导入 Select
from selenium.webdriver.support.ui import Select
# 获得相应的WebElement
select = Select(driver.find_element_by_id("multi"))
# 先去选择所有的 选项
select.deselect_all()
select.select_by_visible_text("雅阁")
select.select_by_visible_text("宝马 740")


# 获得相应的WebElement
select = Select(driver.find_element_by_id("single"))
select.select_by_visible_text("男")

input('press any key to quit...')
driver.quit()   # 浏览器退出