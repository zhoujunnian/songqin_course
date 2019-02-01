import time
def fun1():
    print('in fun1')

def fun2():
    dt = time.strftime('%Y_%m_%d %H:%M:%S',time.localtime())
    print(f"今天是：{dt}")
    return dt

exp = input('请输入表达式:')
ret = eval(exp)
print(ret)