import pymongo

# create client connection
my_client = pymongo.MongoClient("mongodb://localhost:27017")
print("Created client connection.")

# create database
my_db = my_client["w3_database"]
print("Database w3_database created.")

# create collection
my_col = my_db["customers"]
print("Created collection customers in w3_database.")

# check if the collection is created
collection_list = my_db.list_collection_names()
if "customers" in collection_list:
    print("The customers collection exists.")
else:
    print("The customers collection does not exist.")

# insert data into the collection
my_dict = {"name": "John", "address": "Highway 37"}
x = my_col.insert_one(my_dict)
# print the inserted id
print("Inserted data successfully with insert id: ")
print(x.inserted_id)

# insert many data into the collection
my_list = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Side way 1633"}
]
x = my_col.insert_many(my_list)

# print list of the _id values of the inserted documents:
print("Inserted multiple data successfully with insert ids: ")
print(x.inserted_ids)

# create index on the name field
my_col.create_index([("name", pymongo.DESCENDING)], name="w3_database.name")

# create a text index
my_col.create_index([("address", pymongo.TEXT)], name="w3_database.address")

# print multiple documents with specified IDs
my_list = [
    {"_id": 1, "name": "John1", "address": "Highway 371"},
    {"_id": 2, "name": "Peter1", "address": "Lows street 271"},
    {"_id": 3, "name": "Amy1", "address": "Apple st 6521"},
    {"_id": 4, "name": "Hannah1", "address": "Mountain 211"},
    {"_id": 5, "name": "Michael1", "address": "Valley 3451"},
    {"_id": 6, "name": "Sandy1", "address": "Ocean blvd 21"},
    {"_id": 7, "name": "Betty1", "address": "Green Grass 11"},
    {"_id": 8, "name": "Richard1", "address": "Sky st 3311"},
    {"_id": 9, "name": "Susan1", "address": "One way 981"},
    {"_id": 10, "name": "Vicky1", "address": "Yellow Garden 21"},
    {"_id": 11, "name": "Ben1", "address": "Park Lane 381"},
    {"_id": 12, "name": "William1", "address": "Central st 9541"},
    {"_id": 13, "name": "Chuck1", "address": "Main Road 9891"},
    {"_id": 14, "name": "Viola1", "address": "Side way 16331"}
]
x = my_col.insert_many(my_list)

# print list of the _id values of the inserted documents:
print("Inserted multiple data with specific ids successfully with insert ids: ")
print(x.inserted_ids)

# fetch the first record
print("Going to fetch one record.")
x = my_col.find_one()
print(x)

# print all collection records
for x in my_col.find():
    print(x)

# find and print only name and address and not ids
for x in my_col.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)

# exclude address field from the query and print
for x in my_col.find({}, {"address": 0}):
    print(x)

# query by a specific address and print
my_query = {"address": "Park Lane 38"}
my_doc = my_col.find(my_query)
for x in my_doc:
    print(x)

# Find documents where the address starts with the letter "S" or higher:
my_query = {"address": {"$gt": "S"}}
my_doc = my_col.find(my_query)
for x in my_doc:
    print(x)

# find document that starts with letter S
my_query = {"address": {"$regex": "^S"}}
my_doc = my_col.find(my_query)
for x in my_doc:
    print(x)

# find docs sorted by name in ascending order
my_doc = my_col.find().sort("name")
for x in my_doc:
    print(x)

# find docs sorted by name in descending order
my_doc = my_col.find().sort("name", -1)
for x in my_doc:
    print(x)

# limit the query result
my_result = my_col.find().limit(5)
# print the result:
for x in my_result:
    print(x)

# update document address with value "Valley 345" to "Canyon 123"
my_query = {"address": "Valley 345"}
new_values = {"$set": {"address": "Canyon 123"}}
my_col.update_one(my_query, new_values)

# print "customers" after the update:
for x in my_col.find():
    print(x)

# Update all documents which starts with letter S
my_query = {"address": {"$regex": "^S"}}
new_values = {"$set": {"name": "Minnie"}}
x = my_col.update_many(my_query, new_values)
print(x.modified_count, "documents updated.")

# drop index w3_database.name
my_col.drop_index("w3_database.name")

# drop all indexes
my_col.drop_indexes()

# delete document with address "Mountain 21"
my_query = {"address": "Mountain 21"}
my_col.delete_one(my_query)

# delete all documents in collection which start with letter S
my_query = {"address": {"$regex": "^S"}}
x = my_col.delete_many(my_query)
print(x.deleted_count, " documents deleted.")

# delete all documents in collection customers
x = my_col.delete_many({})
print(x.deleted_count, " documents deleted.")

# drop collection customers
my_col.drop()
# check if the collection is created
collection_list = my_db.list_collection_names()
if "customers" in collection_list:
    print("The customers collection failed to get dropped.")
else:
    print("The customers collection dropped successfully.")
