class Tiger:
    classname = 'tiger'

    def __init__(self, weight=200):
        self.weight = weight


    @staticmethod
    def roar():
        print('wow!!!')

    @classmethod
    def roar2(cls, para1):
        print(cls)
        print(cls.classname)


t1 = Tiger(200)

t1.roar2('hello')
Tiger.roar2('hello')

