from selenium import webdriver
import json


def createEasyDriver():
    with  open('session.json') as fh:
        conf = json.loads(fh.read())

    driver = webdriver.Remote(conf['addr'],{})
    driver.session_id = conf['sid']
    driver.w3c = conf['w3c']
    driver.capabilities = conf['capabilities']
    return driver