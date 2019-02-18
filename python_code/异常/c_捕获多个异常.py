# coding=utf-8
try:
    ohmy
    b = 4/0
except ZeroDivisionError:
    print('handle ZeroDivisionError')
except NameError:
    print('handle NameError')

print('结尾处')