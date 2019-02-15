# coding=utf-8
"""
外层取一个，里层循环完，才会回到外层循环
"""
boys  = ['Mike','Jack','Tom']
girls = ['Lisa','Linda','Mary']
for boy in boys:
    for girl in girls:
        print('%s shakes %s' % (boy, girl))
B