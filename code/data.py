import pymongo

myClient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myClient['Test']
myCollection = mydb['Objs']

res = myCollection.delete_many({})

testList = [
    {"_id": 1, "sort": '水果', "name": '橘子', "amount": '2', "want": '梨', "contact": '809953371'},
    {"_id": 2, "sort": '水果', "name": '苹果', "amount": '4', "want": '酸奶', "contact": '809953371'}
]

res = myCollection.insert_many(testList)

print(res)

myquery = {"sort": '水果'}

res = myCollection.find(myquery)

for x in res:
    print(x)

myquery = {"_id": 1}

res = myCollection.delete_many(myquery)

print(res.deleted_count)

myquery = {"sort": '水果'}

res = myCollection.find(myquery)

for x in res:
    print(x)
