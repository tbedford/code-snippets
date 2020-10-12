from tinydb import TinyDB, Query

db = TinyDB('db.json')

print(db.all())

q = Query()
print(db.search(q.name == 'Fred'))
print(db.search(q.age < 40))

