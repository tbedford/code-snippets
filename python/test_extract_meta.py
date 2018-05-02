import re

s = '''
# Generating ISO-8601 dates on Mac OS X

Summary: A question? In this article I describe how you can generate
ISO-8601 format dates on the Mac OS X command line, and also how you
can do it in Python too. Examples: this, and this one; but also this!

Main article text starts here...

---

Published: 2017-10-01 12:21:36 UTC
Updated: 2017-11-10 12:26:00 UTC
UUID: 6768260E-5713-4899-BE43-130BF74DFED2

'''

# title
m = re.search (r'# (.*)', s)
title = m.group(1)
print("Title >%s<" % title)

# Published
m = re.search (r'Published: (.*)', s)
published = m.group(1)
print("Published >%s<" % published)

# Updated
m = re.search (r'Updated: (.*)', s)
updated = m.group(1)
print("Updated >%s<" % updated)

# UUID
m = re.search (r'UUID: ([A-F0-9-]*)', s)
uuid = m.group(1)
print("UUID >%s<" % uuid)

# Summary
#m = re.search(r'Summary: ([\s\w,;!?:.-]*?)\n\n', s)
m = re.search(r'Summary: ([\s\S]*?)\n\n', s)
summary = m.group(1)
print("Summary >%s<" % summary)



