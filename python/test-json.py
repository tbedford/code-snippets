import json

o = {"name": "Tony", "age": 59}
print(o)

s = json.dumps(o)
print(s)

p = json.loads(s)
print(p)

print(p['name'])
print(p['age'])
