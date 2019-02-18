# coding=utf-8
try:
    b = 4/0
    print('abc')    # try里面出现了异常，后面的代码不执行
except ZeroDivisionError:
    print('handle ZeroDivisionError')

print('结尾处')
