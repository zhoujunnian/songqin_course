from random import randint
import time

class Tiger(object):
    classname = 'tiger'

    def __init__(self,weight=200):
        self.weight = weight

    def roar(self):
        print 'wow!!!'
        self.weight -= 5


    def feed(self,food):
        if food == 'meat':
            self.weight += 10
            print 'good, weight + 10'
        else :
            self.weight -= 10
            print 'bad, weight - 10'

class Sheep:
    classname = 'sheep'
    def __init__(self,weight=100):
        self.weight = weight

    def roar(self):
        print 'mie~~'
        self.weight -= 5

    def feed(self,food):
        if food == 'grass':
            self.weight += 10
            print 'good, weight + 10'
        else :
            self.weight -= 10
            print 'bad, weight - 10'

class Room:
    def __init__(self,num,animal):
        self.num = num
        self.animal = animal


rooms = []
for no in range(10):
    if randint(0,1):
        ani = Tiger(200)
    else:
        ani = Sheep(100)

    room = Room(no,ani)
    rooms.append(room)

startTime = time.time()
while True:
    curTime = time.time()
    if (curTime - startTime) > 120:
        print '\n\n **********  game over ********** \n\n'
        for idx, room in enumerate(rooms):
            print 'room :%s' % (idx+1), room.animal.classname, room.animal.weight
        break


    roomno = randint(1, 10)
    room = rooms[roomno-1]  # why -1 ?
    ch = raw_input('in front of room# %s, knock the door?[y/n]' % roomno)
    if ch == 'y':
        room.animal.roar()

    food = raw_input('please feed the animal:')
    room.animal.feed(food.strip())







