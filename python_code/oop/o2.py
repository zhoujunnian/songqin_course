class Tiger(object):
    classname = 'tiger'

    def __init__(self,weight=200):
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

    def __init__(self,weight=200):
        Tiger.__init__(self,weight)

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


neTiger = NeTiger()
scTiger = ScTiger()

print('---- 先看看东北虎 -----')
neTiger.roar()
neTiger.jump()

print('---- 再看看华南虎 -----')
scTiger.roar()
scTiger.jump()

