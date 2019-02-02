# coding=utf-8
import unittest
import run_modul_testcase.feature1.test_m2
import run_modul_testcase.feature2.test_m4

# 使用 模块 加载函数
lfm = unittest.defaultTestLoader.loadTestsFromModule

# 使用 用例 加载函数，这些函数可以将 用例加载起来
lftc = unittest.defaultTestLoader.loadTestsFromTestCase

# 自己定义一个测试套件
ts= unittest.TestSuite()

#  加载 test_m1模块 里面所有的用例
#ts.addTest(lfm(run_modul_testcase.feature1.test_m1))
ts.addTest(lfm(run_modul_testcase.feature1.test_m2))

#  加载 test_m4.WidgetTestCase1类 里面的所有测试用例
ts.addTest(lftc(run_modul_testcase.feature2.test_m4.WidgetTestCase1))

runner = unittest.TextTestRunner()
runner.run(ts)
