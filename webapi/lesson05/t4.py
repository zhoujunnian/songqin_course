# coding=utf8
import requests



response = requests.post("http://localhost/api/mgr/sq_mgr/",
                         data='{"data":34}',
                         headers={'Content-Type':'application/json'},
                         )

rj = response.text
print(rj)



