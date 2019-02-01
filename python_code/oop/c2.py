class Tiger:
    classname = 'tiger'

    def __init__(self, weight=200):
        self.weight = weight

    def tellWeight(self):
        print(f'my weight is {self.weight}')

    @staticmethod
    def roar():
        print('wow!!!')

    @staticmethod
    def roar2():
        print(Tiger.classname)


t1 = Tiger(200)
t2 = Tiger(100)

t1.roar()
t1.roar2()
t1.tellWeight()


t2.roar()
t2.roar2()
t2.tellWeight()



# Tiger.tellWeight()
# Tiger.tellWeight(t1)