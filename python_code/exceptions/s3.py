def f3():
    try:
        print('in f3 - begin')
        b = 4/0
        print('in f3 - end')
    except:
        print('f3中捕获了异常')




def f2():
    try:
        print('in f2 - begin')
        f3()
        print('in f2 - end')
    except:
        print('f2中捕获了异常')


def f1():
    try:
        print('in f1 - begin')
        f2()
        print('in f1 - end')
    except:
        print('f1中捕获了异常')


f1()



    

    
    
    
        

    