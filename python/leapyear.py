import datetime
from calendar import monthrange

y = 1924 # the year to check
m = 2 # Feb has 29 days in leap year

mr = monthrange(y, m)
n = mr[1]

if n == 29:
    print("Leap year - howza!")
elif n == 28:
    print("Not a leap year")
else:
    print("The world will now explode!")



