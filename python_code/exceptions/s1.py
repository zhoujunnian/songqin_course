def f3(): # 乡镇


    print('in f3 - begin')
    b = 4/0
    print('in f3 - end')

def f2(): # 县市
    print('in f2 - begin')
    f3()
    print('in f2 - end')

def f1(): # 省城
    print('in f1 - begin')
    f2()
    print('in f1 - end')

# 中央
f1()
print('底部')



    

    
    
    
        

    