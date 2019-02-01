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
    @classmethod
    def setUpClass(cls):
        print('in setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('in tearDownClass')

    def setUp(self):
        print('in setUp')
        self.widget = Widget('The widget')

    def test_case1_1(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_case9_2(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')

    def tearDown(self):
        print('in tearDown')

if __name__ == '__main__':
    unittest.main()