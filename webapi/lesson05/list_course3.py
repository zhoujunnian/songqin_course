import requests

params = {'action':'list_course', 'pagenum':'1', 'pagesize':20 }
response = requests.get("http://localhost/api/mgr/sq_mgr/",params=params)

r = response.text

print(response.status_code)
print(response.headers)

if response.status_code != 200:
    print ('!!错误, response.status_code != 200')
else:
    print ('正确: response.status_code == 200')


header_ct = response.headers['Content-Type']

if header_ct != 'application/json':
    print ('!!错误, Content-Type != application/json')
else:
    print ('正确: Content-Type == application/json')

# check_equal("response.status_code == 200",response.status_code,200)
# check_equal("response.status_code == 200",'application/json')