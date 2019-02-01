# coding:utf8
import requests,pprint

payload  = {
    'action':'modify_course',
    'id': '459',
    'newdata':'{"name":"初中化学2","desc":"初中化学课程2","display_idx":"4"}'
}

response = requests.put("http://localhost/api/mgr/sq_mgr/",data=payload)


bodyDict = response.json()
pprint.pprint(bodyDict)


