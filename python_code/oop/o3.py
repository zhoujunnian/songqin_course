# coding=utf8
class Tiger:
    classname = 'tiger'

    def __init__(self,weight=100):
        self.weight = weight

    def roar(self):
        print('wow!!!')
        self.weight -= 5

    def feed(self,food):
        if food == 'meat':
            self.weight += 10
            print('good, weight + 10')
        else :
            self.weight -= 10
            print('bad, weight - 10')


class NeTiger(Tiger):
    color = 'yellow white'
    classname = 'northeast tiger'

    def __init__(self,weight=200):
        Tiger.__init__(self,weight)

    def roar(self):
        print('wow!!! wow!!! wow!!!')
        self.weight -= 5

    @staticmethod
    def jump():
        print('3 meters high')


class ScTiger(Tiger):
    color = 'brown black'

    def __init__(self,weight=200):
        Tiger.__init__(self,weight)

    @staticmethod
    def jump():
        print('2 meters high')


tiger = Tiger()
print(tiger.weight)
neTiger = NeTiger()
print(neTiger.weight)
scTiger = ScTiger()

print('---- 先看看东北虎 -----')
neTiger.roar()
neTiger.jump()
print(neTiger.classname)

print('---- 再看看华南虎 -----')
scTiger.roar()
scTiger.jump()


print('---- 再看看老虎 -----')
tiger.roar()

print(scTiger.classname)
