# coding=utf-8
"""
sys模块包含了与python解释器和它的环境有关的函数，这个你可以通过dir(sys)来查看他里面的方法和成员属性。
下面的两个方法可以将模块路径加到当前模块扫描的路径里：
sys.path.append('你的模块的名称')。
sys.path.insert(0,'模块的名称')
永久添加路径到sys.path中，方式有三，如下：
1）将写好的py文件放到 已经添加到系统环境变量的 目录下 ；
2) 在 /usr/lib/python2.6/site-packages 下面新建一个.pth 文件(以pth作为后缀名) (实践可用）
将模块的路径写进去，一行一个路径，如： vim pythonmodule.pth
/home/liu/shell/config
/home/liu/shell/base 
3) 使用PYTHONPATH环境变量
export PYTHONPATH=$PYTHONPATH:/home/liu/shell/config
"""
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


print (__name__)

print (os.__file__)