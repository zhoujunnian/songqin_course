# coding=utf-8

#返回字符串的函数
def hello():
    return 'hello'

def hi():
    return 'hi'

"""
我们需要返回值多俩个感叹号
"""

def endsign(func):
    def wrapper():
        return func()  + ' !!'
    return wrapper

@endsign
def hello():
    return 'hello'
# 等价于 hello = endsign(hello)

print(hello())

