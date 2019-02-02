
def bar():
    print('in bar()')


def foo():
    print('in foo()')
    bar()

foo()

"""
函数里面定义的函数，外部不能调用，目的是，控制函数使用范围
"""


def foo():
    def bar():
        print('in bar()')

    print('in foo()')
    bar()

foo()

"""
如果想给外部程序使用，把函数返回给外部函数，调用外部函数，就是调用里面的函数
"""
def foo():
    def bar():
        print('in bar()')

    print('in foo()')
    return bar

# foo()()
inner = foo()
inner()


"""
函数里面也能定义类
"""
def foo():
    class My():
        pass

    print('in foo()')
    My()

foo()