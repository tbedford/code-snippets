# Dealing with summary

import re

s1 = '''
---
title: Understanding JWTs
summary: >-
  This article takes a look at JSON Web Tokens or JWTs. The article looks at
  their basic format, and how they are created and used.
cat: Code
tags: 'python, jwt'
date_published: 2018-11-01T00:00:00.000Z
date_updated: 2018-11-01T00:00:00.000Z
date_test: 2018-11-01T12:34:56.789Z
---

Stuff here...
'''

s2 = '''
---
title: Understanding JWTs
summary: This article takes a look at JSON Web Tokens or JWTs.
cat: Code
tags: 'python, jwt'
date_published: 2018-11-01T00:00:00.000Z
date_updated: 2018-11-01T00:00:00.000Z
date_test: 2018-11-01T12:34:56.789Z
---

Stuff here...
'''

def fix_summary(s):
    m = re.search(r'summary: >-([\s\S]*?)cat:', s, re.MULTILINE)
    if m: 
        z = m.group(1).strip()
        z = z.replace('\n', '')
        z = z.replace('  ', ' ')
        f = "summary: {z}\ncat:".format(z=z)
        x = re.sub(r'summary: >-[\s\S]*?cat:', f, s, 1) 
        return x
    else:
        return s

print(fix_summary(s1))
print(fix_summary(s2))
