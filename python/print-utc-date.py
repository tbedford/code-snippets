import datetime

x = datetime.datetime.utcnow()
y = x.strftime("%Y-%m-%dT%H:%M:%SZ")
print(x)
print(y)

z = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
print(z)
