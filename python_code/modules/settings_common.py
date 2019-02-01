#-*- coding:utf-8 -*-

# 版本号
VERSION = "0.0.1"

DEBUG = True

SESSION_COOKIE_AGE = 7*24 * 60 * 60  # Age of cookie, in seconds (default: 1 week).

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'services.datamodel.common',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'onme',
        'USER': 'dbadmin',
        'PASSWORD': 'yijiaoqaz',
        'HOST': 'mp.121866.com',
        'PORT': '3306',
        'CONN_MAX_AGE': 0, # 最长连接时间不能太长，否则多个worker的时候，有的worker可能获取不到DB连接
        'OPTIONS': {
               "init_command": "SET storage_engine=INNODB",
        }
    }
}


AUTH_USER_MODEL = 'common.User'

ROOT_URLCONF = 'project.urls'


WSGI_APPLICATION = 'project.wsgi.application'


LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'




RATELIMITTED_CODE = 1001 #API被限速时候的返回码

RATELIMIT_USE_CACHE = 'onedaycache'

# user type 1 means admin, 2 for teacher, 3 for student, 4 for parents
class USER_TYPE:
    ADMIN   = 1
    TEACHER = 2
    STDUENT = 3


class TASK_TYPE:
    EXAM   = 1
    LESSON = 2

# 老师操作频率限制
class TEACHER_OP_RATELIMIT:
    ADD_QUESTION   = '200/d'
    ADD_LESSON     = '30/d'
    ADD_EXAM       = '30/d'



# 短信服务提供商 1： send_mail 2: 阿里大于
class  SMS_SP:
    SELECTED  = 1   # 选择哪个服务商
    SEND_MAIL = 1
    ALI_DAYU  = 2

Courses = [
    {'id':1, 'name':u'基础班'},
    {'id':2, 'name':u'测试开发班'},
]

