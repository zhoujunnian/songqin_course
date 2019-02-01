import requests,pprint


def list_course():

    params = {'action':'list_course', 'pagenum':'1', 'pagesize':20 }
    response = requests.get("http://localhost/api/mgr/sq_mgr/",params=params)

    retDict = response.json()

    pprint.pprint(retDict)
    return retDict['retlist']


def add_course(name,desc,displayidx):
    payload  = {
        'action':'add_course',
        'data': '{"name":"%s","desc":"%s","display_idx":"%s"}' % (name,desc,displayidx)
    }

    response = requests.post("http://localhost/api/mgr/sq_mgr/",
                             data=payload)

    retDict = response.json()
    pprint.pprint(retDict)
    return retDict


def get_new_course(retListBefore,retListAfter):

    newcourse = None
    for one in retListAfter:
        if one not in retListBefore:
            newcourse = one
            break
    return newcourse


