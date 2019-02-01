# coding=utf8
import requests


response = requests.post("http://localhost/api/mgr/sq_mgr/",
                         data='hello',
                         headers={'Content-Type':'application/json'},
                         )

rj = response.text
# print rj.decode("unicode-escape")



