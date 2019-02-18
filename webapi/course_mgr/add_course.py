# coding=utf8
"""
f格式字符串包含大括号包围的“替换字段” {}。任何不包含在大括号中的内容都将被视为文字文本，
并将其原样复制到输出中。如果您需要在文字中包含大括号字符，则可以通过加倍：{{和来避开}}
"""
import requests,json

import time

curTime = time.strftime('%Y-%模块与包-%d',time.localtime(time.time()))

payload  = {
    'action':'add_course',
    'data':f'{{"name":"初学{curTime}","desc":"初中化学课程","display_idx":"1"}}'
}

response = requests.post("http://localhost/api/mgr/sq_mgr/",data=payload)

r = response.json()
print(r)



