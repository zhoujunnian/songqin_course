
# coding:utf8
import requests,json

payload  = {
    'action':'delete_course',
    'id': '452'
}

response = requests.delete("http://localhost/api/mgr/sq_mgr/",data=payload)

r = response.json()
print(r)




