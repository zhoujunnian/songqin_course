from random import  randint
import time,os
import threading


class Tiger:
    classname = 'tiger'
    def __init__(self):
        self.weight = 200

    def roar(self):
        print('wow!!!')
        self.weight -= 5

    def feed(self,food):
        if food == 'meat':
            self.weight += 10
            print('正确，体重 + 10')
        else :
            self.weight -= 10
            print('太惨了，体重 - 10')


class Sheep:
    classname = 'sheep'
    def __init__(self):
        self.weight = 100

    def roar(self):
        print('mie~~')
        self.weight -= 5

    def feed(self,food):
        if food == 'grass':
            self.weight += 10
            print('正确，体重 + 10')
        else :
            self.weight -= 10
            print('太惨了，体重 - 10')


class Room:
    def __init__(self,num,animal):
        self.num = num
        self.animal = animal

rooms = []

for no in range(10):
    if randint(0,1) == 0:
        ani = Tiger()
    else:
        ani = Sheep()

    room = Room(no+1,ani)
    rooms.append(room)


def count_thread():
    # 记录下游戏开始时间
    startTime   = time.time()
    while True:
        time.sleep(0.1)
        curTime = time.time()
        if (curTime - startTime) > 20:
            break

    print(u'游戏结束')
    for room in rooms:
        print(u'房间%s, 里面是%s,体重%s' % (room.num,
                                     room.animal.classname,
                                     room.animal.weight))
    os._exit(0)

t = threading.Thread(target=count_thread)
t.start()


# 循环做如下事情
while True:
    # 提示房间号，让用户选择 敲门 还是 喂食
    curRoomIdx = randint(0,9)
    room = rooms[curRoomIdx]
    print('当前来到房间%s,敲门【q】还是喂食【w】' % room.num)
    ch = input()
    # 如果选择敲门:......
    if ch == 'q':
        room.animal.roar()
    # 如果选择喂食:......
    elif ch == 'w':
        print('请输入食物:')
        food = input()
        room.animal.feed(food)