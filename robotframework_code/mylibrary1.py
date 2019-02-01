import os
from robot.libraries.BuiltIn import BuiltIn

# bi = BuiltIn()
# def my():
#     print 'hello'
#     bi.should_be_equal(1,2)
#
#     print 'world'

def return_list():
    return [1,2]

def _returnlist2():
    return [1,2]

def returndict():
    return {
        'ele1' : 'male',
        'ele2' : 'female'
    }

def printarg(*args,**kwargs):
    if len(args) == 0:
        print('** no args **')
    else:
        print('** args are **')
        print('-----------------')
        for one in args:
            print(repr(one))
        print('-----------------')

    if len(kwargs) == 0:
        print('** no kwargs **')
    else:
        print('** kwargs are **')
        print('-----------------')
        for k,v in kwargs.items():
            print(repr(k) + ':' + repr(v))
        print('-----------------')
