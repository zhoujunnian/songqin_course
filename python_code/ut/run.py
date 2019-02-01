import unittest
import mtf.feature1.test_m1
import mtf.feature2.test_m4

# 使用 模块加载   函数
lfm = unittest.defaultTestLoader.loadTestsFromModule

# 使用 用例加载   函数，这些函数可以将 用例加载起来
lftc = unittest.defaultTestLoader.loadTestsFromTestCase

# 自己定义一个测试套件
ts= unittest.TestSuite()

#  加载模块里面所有的用例
ts.addTest(lfm(mtf.feature1.test_m1))

#  加载类里面的所有测试用例
ts.addTest(lftc(mtf.feature2.test_m4.WidgetTestCase1))

runner = unittest.TextTestRunner()
runner.run(ts)