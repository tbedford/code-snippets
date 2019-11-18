import datetime
from calendar import monthrange

#x = datetime.datetime.now() # Time now

y = 2003
m = 3
d = 20
x = datetime.datetime(y, m, d)
mr = monthrange(y, m)
print("Days in month --> ", mr[1])

for dy in range(1, mr[1]+1):
    dt = datetime.datetime(y, m, dy)
    print(dt.strftime("%a %d %Y"))

