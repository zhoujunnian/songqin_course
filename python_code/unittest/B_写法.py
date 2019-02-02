# coding=utf-8
import unittest

class Widget:
    def __init__(self,msg):
        print(msg)
        self._size = 50,50

    def size(self):
        return self._size

    def resize(self,w,h):
        self._size = w, h

class WidgetTestCase(unittest.TestCase):  # 定义子类，继承父类


    def setUp(self):
        print(' in setUp')
        self.widget = Widget('The widget')

    def tearDown(self):
        print('in tearDown')

    def test_1(self):
        print('in test_1')
        self.assertEqual(self.widget.size(), (50,50),  # assertEqual 是父类的方法，子类也可以用
                         'incorrect default size')

    def test_2(self):
        print('in test_2')
        self.widget.resize(50,150)
        self.assertEqual(self.widget.size(), (50,50),
                         'wrong size after resize')


