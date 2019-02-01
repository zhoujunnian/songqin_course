# please put module_search/d1 to env var PYTHONPATH
import sys

print(sys.path)

import lib1

print(lib1.CONF_ITEM)

lib1.fun1()