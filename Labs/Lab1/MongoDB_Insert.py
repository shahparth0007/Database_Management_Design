import pymongo
client = pymongo.MongoClient("mongodb+srv://team3:qHovInc8WtqPBs7k@newsmonitor.uzcq9.mongodb.net/UserData?retryWrites=true&w=majority")
print(client["territory"])
db = client["Lab_1"]
collection = db["territory"]
print(collection)

territor_dict = {
    'ID': 1,
    'Name': 'Northwest',
    "SalesPersonInfo": 
    [   {"SalespersonID": 274,
        "LastName": "Jiang",
        "TotalSales": 262466},
        {"SalespersonID": 276,
        "LastName": "Mitchell",
        "TotalSales": 2353659},
        {"SalespersonID": 280,
        "LastName": "Ansman-Wolfe",
        "TotalSales": 3748246},
        {"SalespersonID": 281,
        "LastName": "Ito",
        "TotalSales": 848175},
        {"SalespersonID": 283,
        "LastName": "Campbell",
        "TotalSales": 4207895},
        {"SalespersonID": 284,
        "LastName": "Mensa-Annan",
        "TotalSales": 2608116}
    ]
}

print(territor_dict)

rec_id1 = collection.insert_one(territor_dict) 