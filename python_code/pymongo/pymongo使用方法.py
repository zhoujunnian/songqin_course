#!/usr/bin/env python开发
# -*- coding:utf-8 -*-
"""
MongoDB存储
    在这里我们来看一下Python3下MongoDB的存储操作，在本节开始之前请确保你已经安装好了MongoDB并启动了其服务，另外安装好了Python
    的PyMongo库。

连接MongoDB
    连接MongoDB我们需要使用PyMongo库里面的MongoClient，一般来说传入MongoDB的IP及端口即可，第一个参数为地址host，
    第二个参数为端口port，端口如果不传默认是27017。
"""
import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
"""
这样我们就可以创建一个MongoDB的连接对象了。另外MongoClient的第一个参数host还可以直接传MongoDB的连接字符串，以mongodb开头，
例如：client = MongoClient('mongodb://localhost:27017/')可以达到同样的连接效果。
"""
# 指定数据库
# MongoDB中还分为一个个数据库，我们接下来的一步就是指定要操作哪个数据库，在这里我以test数据库为例进行说明，所以下一步我们
# 需要在程序中指定要使用的数据库。

db = client.test
# 调用client的test属性即可返回test数据库，当然也可以这样来指定：
# db = client['temp']
# 　两种方式是等价的。

# 指定集合
# MongoDB的每个数据库又包含了许多集合Collection，也就类似与关系型数据库中的表，下一步我们需要指定要操作的集合，
# 在这里我们指定一个集合名称为students，学生集合。还是和指定数据库类似，指定集合也有两种方式。

collection = db.students
# collection = db['students']
# 插入数据,接下来我们便可以进行数据插入了，对于students这个Collection，我们新建一条学生数据，以字典的形式表示：

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
# 在这里我们指定了学生的学号、姓名、年龄和性别，然后接下来直接调用collection的insert()方法即可插入数据。

result = collection.insert(student)
print(result)
# 在MongoDB中，每条数据其实都有一个_id属性来唯一标识，如果没有显式指明_id，MongoDB会自动产生一个ObjectId类型的_id属性。
# insert()方法会在执行后返回的_id值。

# 运行结果：
# 5932a68615c2606814c91f3d
# 当然我们也可以同时插入多条数据，只需要以列表形式传递即可，示例如下：

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

result = collection.insert([student1, student2])
print(result)
# 返回的结果是对应的_id的集合，运行结果：
# [ObjectId('5932a80115c2606a59e8a048'), ObjectId('5932a80115c2606a59e8a049')]
# 实际上在PyMongo 3.X版本中，insert()方法官方已经不推荐使用了，当然继续使用也没有什么问题，
# 官方推荐使用insert_one()和insert_many()方法将插入单条和多条记录分开。

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

result = collection.insert_one(student)
print(result)
print(result.inserted_id)
# 运行结果：
# <pymongo.results.InsertOneResult object at 0x10d68b558>
# 5932ab0f15c2606f0c1cf6c5
# 返回结果和insert()方法不同，这次返回的是InsertOneResult对象，我们可以调用其inserted_id属性获取_id。

# 对于insert_many()方法，我们可以将数据以列表形式传递即可，示例如下：

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170202',
    'name': 'Mike',
    'age': 21,
    'gender': 'male'
}

result = collection.insert_many([student1, student2])
print(result)
print(result.inserted_ids)
# insert_many()方法返回的类型是InsertManyResult，调用inserted_ids属性可以获取插入数据的_id列表，运行结果：

# <pymongo.results.InsertManyResult object at 0x101dea558>
# [ObjectId('5932abf415c2607083d3b2ac'), ObjectId('5932abf415c2607083d3b2ad')]
# 查询，插入数据后我们可以利用find_one()或find()方法进行查询，find_one()查询得到是单个结果，find()则返回多个结果。

result = collection.find_one({'name': 'Mike'})
print(type(result))
print(result)
# 在这里我们查询name为Mike的数据，它的返回结果是字典类型，运行结果：
# <class'dict'>
# {'_id': ObjectId('5932a80115c2606a59e8a049'), 'id': '20170202', 'name': 'Mike', 'age': 21, 'gender': 'male'}
# 可以发现它多了一个_id属性，这就是MongoDB在插入的过程中自动添加的。

# 我们也可以直接根据ObjectId来查询，这里需要使用bson库里面的ObjectId。

from bson.objectid import ObjectId

result = collection.find_one({'_id': ObjectId('593278c115c2602667ec6bae')})
print(result)
# 其查询结果依然是字典类型，运行结果：

# {' ObjectId('593278c115c2602667ec6bae'), 'id': '20170101', 'name': 'Jordan', 'age': 20, 'gender': 'male'}
# 当然如果查询_id':结果不存在则会返回None。

# 对于多条数据的查询，我们可以使用find()方法，例如在这里查找年龄为20的数据，示例如下：

results = collection.find({'age': 20})
print(results)
for result in results:
    print(result)
# 运行结果：

# <pymongo.cursor.Cursor object at 0x1032d5128>
# {'_id': ObjectId('593278c115c2602667ec6bae'), 'id': '20170101', 'name': 'Jordan', 'age': 20, 'gender': 'male'}
# {'_id': ObjectId('593278c815c2602678bb2b8d'), 'id': '20170102', 'name': 'Kevin', 'age': 20, 'gender': 'male'}
# {'_id': ObjectId('593278d815c260269d7645a8'), 'id': '20170103', 'name': 'Harden', 'age': 20, 'gender': 'male'}
# 返回结果是Cursor类型，相当于一个生成器，我们需要遍历取到所有的结果，每一个结果都是字典类型。

# 如果要查询年龄大于20的数据，则写法如下：

results = collection.find({'age': {'$gt': 20}})
# 在这里查询的条件键值已经不是单纯的数字了，而是一个字典，其键名为比较符号$gt，意思是大于，键值为20，这样便可以查询出所有
# 年龄大于20的数据。

# 在这里将比较符号归纳如下表：
"""
符号含义示例
$lt小于{'age': {'$lt': 20}}
$gt大于{'age': {'$gt': 20}}
$lte小于等于{'age': {'$lte': 20}}
$gte大于等于{'age': {'$gte': 20}}
$ne不等于{'age': {'$ne': 20}}
$in在范围内{'age': {'$in': [20, 23]}}
$nin不在范围内{'age': {'$nin': [20, 23]}}
"""
# 另外还可以进行正则匹配查询，例如查询名字以M开头的学生数据，示例如下：

results = collection.find({'name': {'$regex': '^M.*'}})
# 在这里使用了$regex来指定正则匹配，^M.*代表以M开头的正则表达式，这样就可以查询所有符合该正则的结果。

# 在这里将一些功能符号再归类如下：
"""
符号含义示例示例含义
$regex匹配正则{'name': {'$regex': '^M.*'}}name以M开头
$exists属性是否存在{'name': {'$exists': True}}name属性存在
$type类型判断{'age': {'$type': 'int'}}age的类型为int
$mod数字模操作{'age': {'$mod': [5, 0]}}年龄模5余0
$text文本查询{'$text': {'$search': 'Mike'}}text类型的属性中包含Mike字符串
$where高级条件查询{'$where': 'obj.fans_count == obj.follows_count'}自身粉丝数等于关注数
"""
# 这些操作的更详细用法在可以在MongoDB官方文档找到：
# https://docs.mongodb.com/manual/reference/operator/query/

# 计数
# 要统计查询结果有多少条数据，可以调用count()方法，如统计所有数据条数：

count = collection.find().count()
print(count)
# 或者统计符合某个条件的数据：

count = collection.find({'age': 20}).count()
print(count)
# 排序
# 可以调用sort方法，传入排序的字段及升降序标志即可，示例如下：

results = collection.find().sort('name', pymongo.ASCENDING)
print([result['name'] for result in results])
# 运行结果：

# ['Harden', 'Jordan', 'Kevin', 'Mark', 'Mike']
# 偏移,可能想只取某几个元素，在这里可以利用skip()方法偏移几个位置，比如偏移2，就忽略前2个元素，得到第三个及以后的元素。

results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])
# 运行结果：
# ['Kevin', 'Mark', 'Mike']
# 另外还可以用limit()方法指定要取的结果个数，示例如下：

results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])
# 运行结果：
# ['Kevin', 'Mark']
# 如果不加limit()原本会返回三个结果，加了限制之后，会截取2个结果返回。

# 值得注意的是，在数据库数量非常庞大的时候，如千万、亿级别，最好不要使用大的偏移量来查询数据，很可能会导致内存溢出，
# 可以使用类似find({'_id': {'$gt': ObjectId('593278c815c2602678bb2b8d')}}) 这样的方法来查询，记录好上次查询的_id。

# 更新
# 对于数据更新可以使用update()方法，指定更新的条件和更新后的数据即可，例如：

condition = {'name': 'Kevin'}
student = collection.find_one(condition)
student['age'] = 25
result = collection.update(condition, student)
print(result)
# 在这里我们将name为Kevin的数据的年龄进行更新，首先指定查询条件，然后将数据查询出来，修改年龄，
# 之后调用update方法将原条件和修改后的数据传入，即可完成数据的更新。

# 运行结果：

# {'ok': 1, 'nModified': 1, 'n': 1, 'updatedExisting': True}
# 返回结果是字典形式，ok即代表执行成功，nModified代表影响的数据条数。

# 另外update()方法其实也是官方不推荐使用的方法，在这里也分了update_one()方法和update_many()方法，用法更加严格，
# 第二个参数需要使用$类型操作符作为字典的键名，我们用示例感受一下。

condition = {'name': 'Kevin'}
student = collection.find_one(condition)
student['age'] = 26
result = collection.update_one(condition, {'$set': student})
print(result)
print(result.matched_count, result.modified_count)
# 在这里调用了update_one方法，第二个参数不能再直接传入修改后的字典，而是需要使用{'$set': student}这样的形式，
# 其返回结果是UpdateResult类型，然后调用matched_count和modified_count属性分别可以获得匹配的数据条数和影响的数据条数。

# 运行结果：
#
# <pymongo.results.UpdateResult object at 0x10d17b678>
# 1 0
# 我们再看一个例子：

condition = {'age': {'$gt': 20}}
result = collection.update_one(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)
# 在这里我们指定查询条件为年龄大于20，然后更新条件为{'$inc': {'age': 1}}，执行之后会讲第一条符合条件的数据年龄加1。

# 运行结果：
#
# <pymongo.results.UpdateResult object at 0x10b8874c8>
# 1 1
# 可以看到匹配条数为1条，影响条数也为1条。

# 如果调用update_many()方法，则会将所有符合条件的数据都更新，示例如下：

condition = {'age': {'$gt': 20}}
result = collection.update_many(condition, {'$inc': {'age': 1}})
print(result)
print(result.matched_count, result.modified_count)
# 这时候匹配条数就不再为1条了，运行结果如下：
#
# <pymongo.results.UpdateResult object at 0x10c6384c8>
# 3 3
# 可以看到这时所有匹配到的数据都会被更新。

# 删除
# 删除操作比较简单，直接调用remove()方法指定删除的条件即可，符合条件的所有数据均会被删除，示例如下：

result = collection.remove({'name': 'Kevin'})
print(result)
# 运行结果：
#
# {'ok': 1, 'n': 1}
# 另外依然存在两个新的推荐方法，delete_one()和delete_many()方法，示例如下：

result = collection.delete_one({'name': 'Kevin'})
print(result)
print(result.deleted_count)
result = collection.delete_many({'age': {'$lt': 25}})
print(result.deleted_count)
# 运行结果：

# <pymongo.results.DeleteResult object at 0x10e6ba4c8>
# 1
# 4
# delete_one()即删除第一条符合条件的数据，delete_many()即删除所有符合条件的数据，返回结果是DeleteResult类型，
# 可以调用deleted_count属性获取删除的数据条数。

# 更多
# 另外PyMongo还提供了一些组合方法，如find_one_and_delete()、find_one_and_replace()、find_one_and_update()，
# 就是查找后删除、替换、更新操作，用法与上述方法基本一致。

# 另外还可以对索引进行操作，如create_index()、create_indexes()、drop_index()等。

# 详细用法可以参见官方文档：http://api.mongodb.com/python/current/api/pymongo/collection.html

# 另外还有对数据库、集合本身以及其他的一些操作，在这不再一一讲解，可以参见