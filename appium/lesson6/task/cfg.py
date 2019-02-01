# coding=utf8
MgrLoginUrl  =      'http://localhost/mgr/login/login.html'
StudentLoginUrl=    'http://localhost/student/login/login.html'

database=           ['127.0.0.1'  , '3306']
adminuser=          {'name':'auto'  ,  'pw':'sdfsdfsdf'}
student1=          {'name':'guanyu'  ,  'pw':'sq888',  'realname':u'关羽'}



# 移动应用配置项
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = r'e:\apk\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000