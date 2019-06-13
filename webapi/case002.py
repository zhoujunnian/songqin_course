from webapi import *


# 先登录
loginRet, cookies = login('auto', 'sdfsdfsdf')
if loginRet["retcode"] != 0:
    raise Exception('认证失败')


# 记录下sessionid
sessionid = cookies['sessionid']

# 先添加一门课程
from datetime import datetime
courseName = f'python_{datetime.now().strftime("%Y-%模块与包-%d_%H:%M:%S")}'
retDict1 = add_course(courseName, 'python语言', '2', sessionid)
assert retDict1['retcode'] == 0


# 先列出课程
coureListBefore = list_course(sessionid)['retlist']

# 再添加一门同名课程
retDict = add_course(courseName, 'python语言', '2', sessionid)
assert retDict['retcode'] == 2


# 再列出课程
coureListAfter = list_course(sessionid)['retlist']


# 检查课程没有变化
assert coureListBefore == coureListAfter


# 清除环境操作
for one in coureListBefore:
    if one['name'] == courseName:
        delete_course(one['id'], sessionid)


print('\n========= temp case pass =============')
