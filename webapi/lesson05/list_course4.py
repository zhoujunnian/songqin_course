import requests

params = {'action':'list_course', 'pagenum':'1', 'pagesize':20 }
response = requests.get("http://localhost/api/mgr/sq_mgr/",params=params)

r = response.text


if response.status_code != 200:
    print ('!!错误, response.status_code != 200')
else:
    print ('正确: response.status_code == 20')


bodyDict = response.json()


if bodyDict['total'] != 19:
    print ('!!错误, total number != 19')
else:
    print ('正确: total number == 19')

# check_equal("response.status_code == 200",response.status_code,200)
# check_equal("response.status_code == 200",'application/json')