import requests

params = {'action':'list_course', 'pagenum':'1', 'pagesize':20 }
response = requests.get("http://localhost/api/mgr/sq_mgr/",params=params)

r = response.text

print ('================================')
print(response.status_code)
print(response.headers)
