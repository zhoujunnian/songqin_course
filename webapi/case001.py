from webapi import *


# 先登录
loginRet, cookies = login('auto', 'sdfsdfsdf')
# 判断登陆是否成功
if loginRet["retcode"] != 0:
    raise Exception('认证失败')


# 记录下sessionid
# sessionid是cookies里面的一个键，调用就能获得sessionid的值
sessionid = cookies['sessionid']

# 先列出课程
coureListBefore = list_course(sessionid)['retlist']

# 再添加一门课程
retDict = add_course('python', 'python语言', '2', sessionid)
assert retDict['retcode'] == 0

# 再列出课程
coureListAfter = list_course(sessionid)['retlist']

createCount = len(coureListAfter) - len(coureListBefore)

assert createCount == 1


# 取出，多出来的一门课程对象
newcourse = None
for one in coureListAfter:
    if one not in coureListBefore:
        newcourse = one
        break


# 检查是否是刚刚添加的课程，assert假如没有通过，就会抛异常，就不会执行后面的操作了
assert newcourse is not None
assert newcourse['name'] == 'python'
assert newcourse['desc'] == 'python语言'
assert newcourse['display_idx'] == 2

# 清除环境操作

delete_course(newcourse['id'], sessionid)

print('\n========= test case pass =============')
