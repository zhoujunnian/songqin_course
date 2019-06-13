# coding=utf8

import requests


payload  = {
    'action':'add_course',
    'detect_data':'''{
          "name":"初中化学44",
          "desc":"初中化学课程44",
          "display_idx":"4"
        }'''
}


response = requests.post("http://localhost/api/mgr/sq_mgr/",
                         data=payload)

rj = response.json()
print(rj)



