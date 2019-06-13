# -*- encoding:utf-8 -*-
import requests
import pprint

"""
对资源的操作，都需要合法的账号健全，账号健全有两种方式：session和token是常见的，
sessionid和token都是cookie里面的参数

"""


def login(username, password):
    payload = {
        'username': username,       # 接口文档，post必须带的内容：username，password
        'password': password
    }
    # data参数 就是构造消息体的
    response = requests.post("http://localhost/api/mgr/loginReq",   # 接口文档，登陆的url接口地址
                             data=payload)

    # 获取结果，返回给调用者
    retDict = response.json()
    # 打印出结果
    print(retDict)
    return retDict, response.cookies        # 这个写法就是一个元组


def add_course(name, desc, displayidx, sessionid):
    payload = {
        'action': 'add_course',
        # 格式化字符串的方式来构造消息
        'detect_data': '''
        {
          "name":"%s",
          "desc":"%s",
          "display_idx":"%s"
        }''' % (name, desc, displayidx)

    }
    # data参数 就是构造消息体的
    response = requests.post("http://localhost/api/mgr/sq_mgr/",
                             data=payload,
                             cookies={'sessionid': sessionid})

    # 获取结果，返回给调用者
    retDict = response.json()
    # 打印出结果
    print(retDict)

    return retDict


def list_course(sessionid):

    params = {
        'action': 'list_course',
        'pagenum': '1', 'pagesize': 20
    }
    response = requests.get("http://localhost/api/mgr/sq_mgr/",
                            params=params,
                            cookies={'sessionid': sessionid})
    # 获取结果，返回给调用者
    retDict = response.json()
    pprint.pprint(retDict)

    # 获取结果，返回给调用者
    return retDict


def delete_course(courseid, sessionid):
    payload = {
        'action': 'delete_course',
        'id': f'{courseid}'
    }

    response = requests.delete("http://localhost/api/mgr/sq_mgr/",
                               data=payload,
                               cookies={'sessionid': sessionid})

    r = response.json()
    pprint.pprint(r)
    return r
