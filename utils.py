from app.database import db

def clearAll():
    """clear everything in the database"""
    print 'clear all data in database.'
    cnames = db.collection_names(include_system_collections=False)
    for cname in cnames:
        db[cname].drop()
    print 'done.'

def addDummyClasses(num=10):
    """add some dummy classes to the database"""
    print 'adding ', str(num), ' dummy class to the database.'
    ct = 0
    while ct < 10:
        name = 'Dummy Class ' + str(ct)
        _tid = 'Dummy Teacher Id ' + str(ct)
        db.classes.insert_one({'name': name, '_tid': _tid})
        ct = ct +1
    print 'done.'