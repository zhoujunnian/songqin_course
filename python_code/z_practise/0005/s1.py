# coding=utf8
# 从数据文件中读入文件内容，存入列表recordlist中，其中每个元素对应一条记录

def putInfoToDict(fileName):

    with open(fileName) as f:
        content = f.read()
        recordlist = content.splitlines()


    retDict = {}
    for one in recordlist:
        # one like : 	2017-03-13 11:50:09, 271, 131,
        # 取出其中的 用户id：userid, 签到时间 checkintime, 课程id  lessonid
        one = one.replace('(','').replace(')','').replace("'",'')
        ret = one.split(',')
        checkintime = ret[0].strip()
        lessonid    = ret[1].strip()
        userid      = ret[2].strip()

        # 如果 retDict 没有 userid，

        if userid not in retDict:
            retDict[userid] = [{'lessonid': lessonid,'checkintime':checkintime}]

        # 否则

        else:
            retDict[userid].append({'lessonid': lessonid,'checkintime':checkintime})

    import pprint
    pprint.pprint(retDict)

    return retDict

putInfoToDict('0005_1.txt')