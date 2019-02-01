import requests
import pprint


params = {'action':'list_course', 'pagenum':'1', 'pagesize':20 }
response = requests.get("http://localhost/api/mgr/sq_mgr/",params=params)

bodyDict = response.json()
pprint.pprint(bodyDict)

