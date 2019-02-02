import unittest


def setUpModule():
    print('ts3 setup module')

def tearDownModule():
    print('ts3 teardown module')

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

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')

    def tearDown(self):
        print('in tearDown')