ageTable = '''
    诸葛亮, 28
    刘备, 48
    刘琦, 25
    赵云, 32
    张飞, 43
    关羽, 45
'''



# 先转换成如下格式的列表
# ageList = [
#     '诸葛亮, 28',
#     '刘备, 48',
#     '赵云, 42',
#     ....
# ]

ageList = []
for item  in ageTable.split('\n'):
    # 跳过空行
    if item.strip()  == '':
        continue

    ageList.append(item)

g30 = []  # 大于30岁人员列表
l30 = []  # 小于30岁人员列表
for oneman  in ageList:
    name,age   = oneman.split(',')
    age = int(age.strip())
    name = name.strip()
    if age >= 30:
        g30.append(name)
    else:
        l30.append(name)


print('大于等于30岁的人有：')
for man in g30:
    print(man)


print('\n小于30岁的人有：')
for man in l30:
    print(man)