import unittest

class Widget:
    def __init__(self,msg):
        # print(msg)
        self._size = 50,50

    def size(self):
        return self._size

    def resize(self,w,h):
        self._size = w, h

class WidgetTestCase(unittest.TestCase):


    def setUp(self):
        print('in setUp')
        self.widget = Widget('The widget')
        raise Exception()

    def tearDown(self):
        print('in tearDown')

    def test_case1_1(self):
        print('in test_case1_1')
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_case1_2(self):
        print('in test_case1_2')
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
