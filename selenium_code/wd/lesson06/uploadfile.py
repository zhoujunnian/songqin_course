
from selenium import webdriver

import time

driver = webdriver.Chrome(r"d:\tools\webdrivers\chromedriver.exe")
driver.implicitly_wait(10)


driver.get('http://121866.com/cust/anonym_page.html')
print(driver.title)

driver.find_element_by_id("pick_pic_files").click()



time.sleep(3)

# 直接发送键盘消息给 当前应用程序，
# 前提是浏览器必须是当前应用
#   pip install pypiwin32
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")
shell.Sendkeys(r"d:\p1.jpg" + '\n')


input('...')

driver.quit()