# coding=utf-8

"""
有参数的函数
"""
def endsign(func):
    def wrapper(*args,**kargs):
        print('args:',args)
        print('kargs:',kargs)
        return func(*args,**kargs) + ' !!'
    return wrapper

@endsign
def hello(arg1,arg2=''):
    print('arg1:',arg1)
    print('arg2:',arg2)
    return 'hello %s %s' % (arg1,arg2)
# hello = endsign(hello)

@endsign
def goodbye(targets):
    return 'goodbye %s ' % ' '.join(targets)


# print(hello('cat', 'dog'))
# print('=====================\n')
print(hello('cat', arg2='dog'))
# print('=====================\n')
print(goodbye(['jack', 'lisa', 'tom', 'mike']))

