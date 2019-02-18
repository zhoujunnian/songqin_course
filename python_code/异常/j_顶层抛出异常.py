# coding=utf-8
def f3():
    print('in f3 - begin')
    b = 4/0
    print('in f3 - end')


def f2():
    print('in f2 - begin')
    f3()
    print('in f2 - end')


def f1():
    try:
        print('in f1 - begin')
        f2()
        print('in f1 - end')
    except:
        print('!!!!')


f1()
print('底部')



    

    
    
    
        

    