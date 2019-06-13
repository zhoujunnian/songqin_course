# coding=utf8
import requests



response = requests.post("http://localhost/api/mgr/sq_mgr/",
                         data='{"detect_data":34}',
                         headers={'Content-Type':'application/json'},
                         )

rj = response.text
print(rj)



