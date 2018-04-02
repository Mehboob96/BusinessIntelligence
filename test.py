from pymongo import MongoClient
import pprint
client = MongoClient('mongodb://localhost:27017/')
doc = {
    "surname" : "Shaikh",
    "first_name" : "Mehboob",
    "last_name" : "Siraj",
    "age" : 21,
    "gender" : "male",
    "qualification" : "BE in Computer Engineering",
    "contact" : {
        "Mummy" : 8691996893,
        "Dad" : 9702475201,
        "personal" : 9702020991
    }
}

db = client.example
db.personalDetail.insert(doc)

for a in db.personalDetail.find():
    pprint.pprint(a)
