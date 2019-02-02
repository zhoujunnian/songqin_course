# coding=utf-8
"""
我们在写模块文件的时候，对里面对函数往往有些测试代码，调用一下上面写对函数，
如果忘来注释掉，在其他模块导入这个模块对时候，就会执行，所以在把测试代码放
在if __name__ == "__main__"下面执行，就可以了
"""
def sayHello():
    print ("hello")

def sayGoodbye():
    print ("goodbye")

print("m3 name is " + __name__)

if __name__ == "__main__":
    print ('exec testing')
    sayHello()
    sayGoodbye()
