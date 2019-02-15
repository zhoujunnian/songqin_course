# coding=utf-8

"""
python子类如何调用父类的__init__方法(网上摘录）

Python不会自动调用父类的constructor，你得亲自专门调用它。

两种方法：

父类名.__init__(self, 参数)  # 注意名字是父类
super(子类名, self).__init__(参数)  # 注意名字是子类，而且init后是self之外的参数

第一种方法，这种初始化的方式书写上比较简单，也比较容易阅读。

举个栗子：
"""


class Person(object):
    def __init__(self, name="jim"):
        self.name = name
        self.flag = False
        print "Person", self.name

    def call(self):
        print self.flag, "name:", self.name
        self.flag = not self.flag


class Programmer(Person):
    def __init__(self):
        Person.__init__(self, "Dotjar")
        print "Programmer"

    def set_name(self, name):
        self.name = name

coder = Programmer()
coder.call()
coder.set_name("dotjar")
coder.call()

"""
该例子中，Programmer实例初始化的时候调用父类的__init__方法对flag属性进行初始化，初始化之后的属性值是False。
注意，调用父类__init__方法的时候，传递的参数数量要与父类中的__init__保持一致。
程序运行结果是：

Person Dotjar
Programmer
False name: Dotjar
True name: dotjar

注意：运行的时候如果你的环境里有多个python解释器，一定要选对解释器了，否则有的时候可能会出错。运行程序的时候，最后打个断点debug一下，看看程序运行的步骤。

第二种方法，举个栗子：
"""

class Person(object):
    def __init__(self, flag=False, name="jim"):
        self.name = name
        self.flag = flag
        print "Person", self.name

    def call(self):
        print self.flag, "name:", self.name
        self.flag = not self.flag


class Programmer(Person):
    def __init__(self, flag=True, name="Dotjar", age=19):
        self.age = 19
        super(Programmer, self).__init__(flag, name)
        print "Programmer's age:", self.age

    def set_name(self, name):
        self.name = name


coder = Programmer()
coder.call()
coder.set_name("dotjar")
coder.call()

"""
这个例子对第一个例子进行了修改，首先父类中的__init__方法带有2个初始化属性，flag和name。子类的__init__方法比父类的__init__方法多了一个age属性，
这个age属性只能在子类的__init__方法中初始化（因为父类中没有嘛，调用父类的__init__只能初始化父类和子类共有的属性）。

程序的输出是：

Person
Dotjar
Programmer's age: 19
True
name: Dotjar
False
name: dotjar
"""