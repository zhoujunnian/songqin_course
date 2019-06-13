# coding:utf8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class WebOp:

    shared_wd = None


    def openBrowser(self):
        if WebOp.shared_wd :
            return

        WebOp.shared_wd = webdriver.Chrome()

        WebOp.shared_wd.implicitly_wait(1.5)





    def closeBrowser(self):
        WebOp.shared_wd.quit()