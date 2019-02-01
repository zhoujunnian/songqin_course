# coding=utf8

import util
driver = util.createEasyDriver()


driver.get('http://www.baidu.com') # 打开网址
ele = driver.find_element_by_id('kw')
ele.send_keys(u'张学友\n')

print driver.current_url

