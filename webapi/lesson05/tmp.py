# coding=utf8

import requests


payload  = '''<name>姚明</name> 
           <height>225cm</height>'''.encode()


response = requests.post("http://localhost/apijson/mgr/sq_mgr/",
                         data=payload)

rj = response.json()
print(rj)