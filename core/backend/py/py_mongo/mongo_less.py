import datetime

from pymongo import MongoClient


client = MongoClient("mongodb://admin:pymong@mongo:27017/")
db = client["test_database"]
collection = db["test_table"]


data = {
    "id": "a100",
    "name": ["satou"],
    "department": {"vegetables": "carrot"},
    "date": datetime.datetime.utcnow()
}

# データ挿入するにはinsert_oneメソッド使用
inserted_data = collection.insert_one(data)
print(data)
print(inserted_data.inserted_id)