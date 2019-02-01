# coding=utf8

# 读取文件内容
fh = open('debug.txt')
content = fh.read()
fh.close()

# 将学生年龄信息存入age2names中
students = content.split(',')

age2names = {}
for student in students:

    name, age = student.split(':')
    name = name.strip()
    age  = age.strip()

    if age in age2names:
        age2names[age].append(name)
    else:
        age2names[age] = [name]

curMax = 0
maxCountAge = 0
# 根据age2names 计算出人数最多的年龄
for age, names in age2names.items():
    count = len(names)
    if count >= curMax:
        curMax = count
        maxCountAge = age

print 'maxCountAge :%s' % maxCountAge



