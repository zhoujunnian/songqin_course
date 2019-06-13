# !/usr/bin/python开发
# -*- coding:utf-8 -*-
# Time    : 2019-05-12 16:00
# author  : Zhoujunjun
# File    : g.touchaction.py
# Software: PyCharm

# coding=utf8

# appium 库导入webdriver 对象，点击查看一下该对象，讲解webdriver是个package目录，
# import目录，其实就是执行下面的__init__.py。其包含的标识符是决定的
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time,traceback


# 这里定义的 desired_capabilities，作为下面 webdriver.Remote
# 初始化一个webdriver的参数。
# 这些键值对告诉appium server 测试程序希望进行的是什么什么样的测试
# 比如下面 platformName  和 platformVersion 两个配置项
# desired_caps = {}
desired_capabilities = {}
desired_capabilities['platformName'] = 'Android'  #测试平台,不能写错
desired_capabilities['automationName'] = 'Appium'  #测试平台,不能写错
desired_capabilities['platformVersion'] = '5.1'   #平台版本,不能写错
# 设备名称，其实没有太大的用处，只是给测试程序使用的
desired_capabilities['deviceName'] = '192.168.56.104:5555'
# apk 文件路径名，如果设备还没有此应用，则会安装。 什么是apk文件？
desired_capabilities['app'] = '/Users/zhoujunjun/Downloads/toutiao.apk'
# app package名，一定要有，是每个app 的ID，唯一标识了这个app。
# 安卓上运行某个app，不是根据它的路径而是appid ，也就是这package name
# 怎么获取？后面会讲
desired_capabilities['appPackage'] = 'io.manong.developerdaily'
# app默认Activity，也是必须的参数。Activity 的概念后面会讲述，
# 目前我们就理解为一个用户操作界面就可以了
# 怎么获取？后面会讲
desired_capabilities['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
# 一定要有该参数，否则测试过程中无法输入中文
# 加上这个参数会新加一种unicode输入法
desired_capabilities['unicodeKeyboard']  = True
# 保证了app 测试前不会清除数据，缺省是会清除数据的，
desired_capabilities['noReset'] = True
# How long (in seconds) Appium will wait for a new command from
# the client before assuming the client quit and ending the session
desired_capabilities['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
el2 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.view.View/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView")
el2.click()
TouchAction(driver).move_to(x=970, y=733)
TouchAction(driver).press(x=996, y=1796).move_to(x=996, y=821).release().perform()
