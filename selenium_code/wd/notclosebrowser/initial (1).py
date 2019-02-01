# coding=utf8

'''
我们需要修改  webdriver.py 

    将  class WebDriver(object): 里面 的
        self.start_session(desired_capabilities, browser_profile)
    
    加上一个判断条件：
        if desired_capabilities:
            self.start_session(desired_capabilities, browser_profile)

'''
from selenium import webdriver
import json


executable_path = r"d:\tools\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path) #初始化，运行chrome driver



with open('session.json','w') as fh:
    content = {
        'addr': driver.command_executor._url,
        'sid': driver.session_id,
        'w3c': driver.w3c,
        'capabilities': driver.capabilities,
    }
    fh.write(json.dumps(content))





