# coding=utf-8
import traceback
try:
    while True:
        num = input('** 请输入数字:')
        if num.isdigit():
            print('立方是 : %s' % int(num) ** 3)
except:
    print(traceback.format_exc())
    pass

