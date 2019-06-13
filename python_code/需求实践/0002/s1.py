# coding=utf8
# 请用户输入学生年龄信息，程序读入信息， 存入一个变量 studentsInfo

studentsInfo = input('please input students info:')

#将 变量 studentsInfo 中的 每个学生信息 存入列表infoList中，作为一个元素
# [
#     'Jack Green ,   21',''
#     'Mike Mos, 9',
#     'Mary Josn, 30'，
#
#     。。。。。
# ]
infoList = studentsInfo.split(';')

# 对 infoList中，每个 元素， 做如下如理：
#     取出 用户名部分 name 和年龄部分 age， 格式化成如下结果
#     Jack Green :   21;

for one in infoList:
    if one.count(',') != 1:
        continue
    name,age = one.split(',')
    name = name.strip()
    age = int(age.strip())
    print('{:20} :   {:02}'.format(name, age))
