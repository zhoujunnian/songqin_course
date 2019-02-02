import unittest

class Widget:
    def __init__(self,msg):
        # print(msg)
        self._size = 50,50

    def size(self):
        return self._size

    def resize(self,w,h):
        self._size = w, h

class WidgetTestCase1(unittest.TestCase):


    def setUp(self):
        print('in setUp')
        self.widget = Widget('The widget')

    def tearDown(self):
        print('in tearDown')

    def test_6(self):
        print('in test_6')
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_7(self):
        print('in test_7')
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')



class WidgetTestCase2(unittest.TestCase):


    def setUp(self):
        print('in setUp')
        self.widget = Widget('The widget')

    def tearDown(self):
        print('in tearDown')

    def test_8(self):
        print('in test_8')
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_9(self):
        print('in test_9')
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')



