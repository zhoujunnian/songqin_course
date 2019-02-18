# coding=utf-8
try:
    ohmy
except NameError as e:      # python3用的是as，python2用的是逗号，
    print(type(e))
    print('handle NameError:', e)

