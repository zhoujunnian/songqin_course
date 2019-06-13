# 有两个参数
def getNameAge(str1, str2):
    # 用切片获取第1个参数的人名
    name = str1[-2:]

    # 用切片获取第2个参数的 年龄
    age = str2[-2:]

    # 将人名和 年龄连起来，中间是冒号

    ret = name + ':' + age

    # 别忘了， 最后一定要使用return 返回结果
    return ret

# 不指定参数名的调用
name_age1 = getNameAge('他的名字是：关羽','他的年龄是：28')
# 打印出返回结果
print(name_age1)


# 指定参数名的调用
name_age2 = getNameAge(str1='他的名字是：赵云',str2='他的年龄是：24')
# 打印出返回结果
print(name_age2)