def foo():
    def bar():
        print('in bar()')

    print('in foo()')
    return bar

# foo()()
inner = foo()
inner()
