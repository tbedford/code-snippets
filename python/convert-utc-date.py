import re

# 1. date -u +"%Y-%m-%dT%H:%M:%SZ"
# UTC date: 2019-11-01T10:50:42Z
# 2. 2018-11-01T12:34:56.789Z

# Convert this to just date
def convert_iso_utc(s):
    m = re.search (r'(\d\d\d\d-\d\d-\d\d)T(\d\d:\d\d:\d\d)', s)
    date = m.group(1)
    time = m.group(2)
    return date + ' ' + time

s1 = "2019-11-01T10:50:42Z"
s2 = "2018-11-01T12:34:56.789Z"
print(convert_iso_utc(s1))
print(convert_iso_utc(s2))

