import requests,pprint

params = {'action':'list_course', 'pagenum':'1', 'pagesize':20 }

response = requests.get("http://localhost/api/mgr/sq_mgr/",
                        params=params)




retTxt = response.text
print(retTxt)
pprint.pprint(response.json())

res = response.json()
print('检查返回吗')
if res['retcode'] != 0:
    print('返回码不是0！！！')
else:
    print('检查通过')

found = False
for one in   res['retlist']:
    if one['id'] == 3434904:
        found = True

if found:
    print('找到id是3434904的课程')
else:
    print('!!没有找到id是3434904的课程')