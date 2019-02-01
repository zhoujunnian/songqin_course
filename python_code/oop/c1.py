class Tiger:
    classname = 'tiger'

    def __init__(self, weight=200):
        print 'haha, in __init__'
        self.weight = weight

    def roar(self):
        print 'self wow!!!'
        print self.weight

    @staticmethod
    def roar2():
        print 'wow!!!'

    @staticmethod
    def roar3():
        print Tiger.classname

t1 = Tiger()
t1.roar()
t1.roar2()
t1.roar3()