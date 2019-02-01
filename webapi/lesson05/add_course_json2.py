import requests,json

# 3个参数，根据参数来发送相应的消息
def add_course_json(name,desc,displayidx):
    payload = {
        'action': 'add_course_json',
        # 格式化字符串的方式来构造消息
        'data':
        {
          "name":name,
          "desc":desc,
          "display_idx":displayidx
        }

    }

    # data参数 就是构造消息体的
    # 可以使用 data=json.dumps(payload)
    #  也可以使用 json=payload
    response = requests.post("http://localhost/apijson/mgr/sq_mgr/",
                             data=json.dumps(payload),
                             headers = {'Content-Type':'application/json'})



    # 获取结果，返回给调用者
    retDict = response.json()
    # 打印出结果
    print(retDict)
    return retDict



add_course_json('哈哈','嘻嘻',1)