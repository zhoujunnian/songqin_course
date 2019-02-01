# coding=utf8

import requests


headers = {
    'user-agent': 'jcyapptest/0.0.1',
    'username': 'patrick',
    'password' : '111111'
}

response = requests.get("http://localhost/api/mgr/sq_mgr/",
                        headers=headers)

rj = response.text
print(rj)



