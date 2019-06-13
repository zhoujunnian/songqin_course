import requests,pprint

def list_course():

    params = {'action':'list_course', 'pagenum':'1', 'pagesize':20 }
    response = requests.get("http://localhost/api/mgr/sq_mgr/",params=params)

    retDict = response.json()

    pprint.pprint(retDict)
    return retDict['retlist']

# 先列出课程
retListBefore = list_course()

# 再添加一门课程
payload  = {
    'action':'add_course',
    'detect_data': '{"name":"python开发","desc":"python语言","display_idx":"2"}'
}

response = requests.post("http://localhost/api/mgr/sq_mgr/",data=payload)

retDict = response.json()
assert retDict['retcode'] == 0


# 再列出课程
retListAfter = list_course()


# 取出，多出来的一门课程对象
newcourse = None
for one in retListAfter:
    if one not in retListBefore:
        newcourse = one
        break

# 检查是否是刚刚添加的课程
assert newcourse!=None
assert newcourse['name']=='python开发'
assert newcourse['desc']=='python语言'
assert newcourse['display_idx']==2

print('temp case pass')
