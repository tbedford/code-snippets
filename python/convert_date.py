# Convert date from
# 2017-10-01 12:21:36 UTC format to
# 2017-11-10T13:28:59Z
# NOTE: I use UTC dates/times ONLY as would be obtained with:
# date -u +"%Y-%m-%dT%H:%M:%SZ"
# I NEVER use the format that shows time difference to UTC.

import re

def convert_date1 (s):

    print("Input date: %s" % s)
    
    m = re.search (r'(\d\d\d\d-\d\d-\d\d)', s)
    date = m.group(1)

    m = re.search (r'(\d\d:\d\d:\d\d)', s)
    time = m.group(1)

    iso_date = date + "T" + time + "Z"

    return iso_date

def convert_date3 (s):

    print("Input date: %s" % s)

    m = re.search (r'(\d\d\d\d-\d\d-\d\d) (\d\d:\d\d:\d\d) (\w\w\w)', s)

    if m.group(3) != "UTC":
        print("ERROR: Only UTC format should be specified!")
        exit(-1)

    return m.group(1) + "T" + m.group(2) + "Z"

#print (convert_date1 ("2017-10-01 12:21:36 UTC"))
print (convert_date3 ("2017-05-03 09:01:45 UTC"))


# Convert the following format
# Obtained with date -u
# Tue 14 Nov 2017 09:29:15 UTC
# To:
# 2017-11-14T09:29:15Z

def convert_date2 (s):

    print("Input date: %s" % s)

    months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    
    m = re.search (r'(\w\w\w) (\d\d) (\w\w\w) (\d\d\d\d) (\d\d:\d\d:\d\d) (\w\w\w)', s)

    if m.group(6) != "UTC":
        print("Only UTC format should be specified!")
        exit(-1)
    
    
    YYYY = m.group(4)
    MM = str(months[m.group(3)])
    DD = m.group(2)
    time = m.group(5)
    
    return YYYY + '-' + MM + '-' + DD + 'T' + time + 'Z'


#print(convert_date2 ("Tue 14 Nov 2017 09:29:15 UTC"))

