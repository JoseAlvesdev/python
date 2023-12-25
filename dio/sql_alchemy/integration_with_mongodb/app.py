import pymongo as pyM

client = pyM.MongoClient('mongodb+srv://josehenriques10:6012Je10Hq@cluster0.odjelhd.mongodb.net/?retryWrites=true&w=majority')

db = client.test
collection = db.test_collection

# Definição de infos para compor o documento
post = {
    "author": "Mike",
    "text": "My first mongodb application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# Preparando para submeter as infos
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)