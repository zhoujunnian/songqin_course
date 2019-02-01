def foo():
    def bar():
        print('in bar()')

    print('in foo()')
    bar()

foo()
