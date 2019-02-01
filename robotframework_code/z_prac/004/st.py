# coding:utf8
from selenium import webdriver
import time

executable_path = r"d:\tools\webdrivers\chromedriver.exe"


def  deleteAllLesson():
    driver = webdriver.Chrome(executable_path)
    driver.implicitly_wait(4)

    driver.get('http://localhost/mgr/login/login.html')



    driver.find_element_by_id('username').send_keys('auto')
    driver.find_element_by_id('password').send_keys('sdfsdfsdf')
    driver.find_element_by_tag_name('button').click()


    # 界面重新生成了，下面的代码会有问题

    # deleteButtons = driver.find_elements_by_css_selector("button[ng-click^='delOne']")
    # for one in deleteButtons:
    #     one.click()
    #     driver.find_element_by_css_selector('button.btn-primary').click()

    #应这样写


    driver.implicitly_wait(1)
    while True:
        deleteButtons = driver.find_elements_by_css_selector("button[ng-click^='delOne']")
        if deleteButtons:
            deleteButtons[0].click()
            driver.find_element_by_css_selector('button.btn-primary').click()
            time.sleep(1)

        else:
            break

    driver.implicitly_wait(10)

    driver.quit()
