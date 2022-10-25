import pymongo

klien = pymongo.MongoClient("mongodb://localhost:27017/")
db_toko = klien["toko"]
koleksi = db_toko["jual"]

koleksi.drop()

print(db_toko.list_collection_names())
