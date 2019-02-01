# 读取文件内容


def getFileContent(filePath):
    fh = open(filePath)
    fc = fh.read()
    fh.close()
    return fc

content = getFileContent('debug.txt')

# 将学生年龄信息存入age2names中
students = content.split(',')

age2names = {}
for student in students:
    name, age = student.split(':')
    if age in age2names:
        age2names[age].append(name)
    else:
        age2names[age] = [name]


curMax = 0                # 人数最多的年龄  的人数 ，初识值设置为  0
maxCountAge = None        # 人数最多的年龄   ，初识值设置为  None

# 根据age2names 计算出人数最多的年龄
for age, names in age2names.items():

    count = len(names)
    if count >= curMax:
        curMax = count
        maxCountAge = age

print('人数最多的年龄是 %s岁' % maxCountAge)



