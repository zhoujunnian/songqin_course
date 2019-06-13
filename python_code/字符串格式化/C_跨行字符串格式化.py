#  -*- coding:utf-8 -*-
vs = [('Jack',8756),('Patrick',10000)]

# 跨行字符串，用3个引号
fs = '''
%s salary: %d $
%s salary: %d $
'''

print(fs % (vs[0][0], vs[0][1], vs[1][0], vs[1][1]))
