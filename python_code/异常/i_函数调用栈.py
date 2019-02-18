# coding=utf-8
def f3(): # 乡镇


    print('in f3 - begin')
    b = 4/0     # 这里出现了异常，代码不能执行下去
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

"""
异常从调用栈里面抛出：
类似，中央——省城——县市——乡镇，下达政策；
出现异常，会在当前找能否处理这种异常，如果没有，往上找，再没有，再往上找，还是找不到，就抛出异常；
在任何层加上处理异常，都不会抛出异常
"""

    

    
    
    
        

    