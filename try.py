from pymongo import MongoClient

# Connect to MongoDB server
client = MongoClient('localhost', 27017)

# Access a database (if it doesn't exist, it will be created)
db = client['mydatabase']

# Access a collection within the database (if it doesn't exist, it will be created)
collection = db['mycollection']

# Insert a document into the collection
post = {"author": "John Doe",
        "text": "My first MongoDB post!",
        "tags": ["mongodb", "python", "pymongo"]}
inserted_post = collection.insert_one(post)
print("Inserted document ID:", inserted_post.inserted_id)

# Find documents in the collection
cursor = collection.find({"author": "John Doe"})
for document in cursor:
    print("Found document:", document)

# Update a document in the collection
update_result = collection.update_one({"author": "John Doe"}, {"$set": {"text": "Updated MongoDB post!"}})
print("Modified document count:", update_result.modified_count)


# Find documents in the collection
cursor = collection.find({"author": "John Doe"})
for document in cursor:
    print("Found document:", document)

# Delete a document from the collection
delete_result = collection.delete_one({"author": "John Doe"})
print("Deleted document count:", delete_result.deleted_count)

#add another value
post = {"author": "John Doe",
        "text": "My first MongoDB post!",
        "tags": ["mongodb", "python", "pymongo"]}
inserted_post = collection.insert_one(post)
print("Inserted document ID:", inserted_post.inserted_id)

# Find documents in the collection
cursor = collection.find()
for document in cursor:
    print("Found document:", document)

# Disconnect from the MongoDB server
client.close()
