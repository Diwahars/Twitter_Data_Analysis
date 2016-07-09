from pymongo import MongoClient

client = MongoClient()
db = client.test

cursor = db.std.find()
print cursor
for document in cursor:
    print(document)
    print("\n")