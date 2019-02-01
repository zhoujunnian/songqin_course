# coding:utf8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from cfg import *
import time
from robot.api import logger
from pylib.WebOp import WebOp

class WebOpStudent(WebOp):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'



    def loginWebSite(self,username,passwd):
        WebOp.shared_wd.get(StudentLoginUrl)

        WebOp.shared_wd.find_element_by_id('username').send_keys(username)
        WebOp.shared_wd.find_element_by_id('password').send_keys(passwd)
    
        WebOp.shared_wd.find_element_by_tag_name('button').click()


    def EnterTab(self,name):

        tabLinkCss =  u'div.main-menu a[href$={}]  li'.format(name)
        WebOp.shared_wd.find_element_by_css_selector(tabLinkCss).click()
        time.sleep(1)


    def CheckIn(self):
        self.EnterTab('checkin')

        time.sleep(2)
        WebOp.shared_wd.find_element_by_css_selector('button[ng-click^=checkin]').click()

        WebOp.shared_wd.find_element_by_css_selector('.bootstrap-dialog-footer-buttons button').click()

        time.sleep(2)


def test():
    wo = WebOpStudent()
    # 打开浏览器，创建webdrier




if __name__ == '__main__':
    test()