import pymongo

db = None

def init_db(config_obj):
    global db
    client  = pymongo.MongoClient(config_obj.MONGODB_URI)
    db = client[config_obj.MONGODB_DB]
    return db