class Tiger(object):
    classname = 'tiger'

    def __init__(self,weight=200):
        self.weight = weight

    def roar(self):
        print('wow!!!')
        self.weight -= 5

class Sheep:
    classname = 'sheep'
    def __init__(self,weight=100):
        self.weight = weight

    def roar(self):
        print('mie~~')
        self.weight -= 5


class Room:
    def __init__(self, num,animal):
        self.num = num
        self.animal = animal



t1 =  Tiger(300)
room1 = Room(1,t1)

s1 =  Sheep(80)
room2 = Room(2,s1)

print(room1.num, room1.animal.classname)
print(room2.num, room2.animal.classname)
room1.animal.roar()
room2.animal.roar()



