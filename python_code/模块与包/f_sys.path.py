# coding=utf-8
import sys
import os
print(sys.path)
#sys.path.append(r'PycharmData/git_hub/songqin_course/python_code/模块与包/module_search/d1')
#sys.path.append('module_search/d1')
print(sys.path)
from git_hub.songqin_course.python_code.模块与包.module_search.d1 import lib1       # 1.如果把__init__.py删除，就不能导入;2.有中文名也不可以
from module_search.d1 import lib1

print(lib1.__file__)
print(lib1.fun1())

print(lib1.CONF_ITEM)


print __name__

print os.__file__