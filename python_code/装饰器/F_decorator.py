# coding=utf-8
"""
装饰器本身带参数
"""
# 原理
def decorator(argument):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + argument
        return wrapper
    return real_decorator

# 例子
def endsign(tail):
    def innerOne(func):
        def wrapper():
            return func()  + ' ' + tail
        return wrapper
    return innerOne

@endsign('333')
def hello():
    return 'hello'
# hello = endsign('333') (hello)

print(hello())

