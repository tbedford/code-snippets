# \s Returns a match where the string contains a white space character
# \S Returns a match where the string DOES NOT contain a white space character

import re

s1 = '''
---
meta1: meta data 1
meta2: meta data 2
meta3: 2019-01-21
---

content 1
content 2
---
'''

# Greedy *? to for matched delimiters
def extract(source):
    m = re.search(r'---([\s\S]*?)---', source, re.MULTILINE)
    print(m)
    return m.group(1).strip()

print(extract(s1))
