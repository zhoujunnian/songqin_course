def bar():
    print('in bar()')


def foo():
    print('in foo()')
    bar()


foo()
