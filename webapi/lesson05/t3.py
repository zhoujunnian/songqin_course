# coding=utf8

import requests

import json

payload ={
    "name":"初中化学2",
    "desc":"初中化学课程2",
    "display_idx":"4"
}


response = requests.post("http://localhost/api/mgr/sq_mgr/",
                         data=json.dumps(payload),
                         headers = {'Content-Type':'Application/json'})

rj = response.text
print(rj)



