import sys

print(sys.path)
sys.path.append(r'd:\gsync\workspace\sq\python\samples\modules\module_search\d1')
#sys.path.append('module_search/d1')
print(sys.path)

import lib1

print(lib1.__file__)
print(lib1.fun1())

print(lib1.CONF_ITEM)

