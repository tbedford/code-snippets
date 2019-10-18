import re

s = '''
---
meta1: meta data 1
meta2: meta data 2
---

content 1
content 2
---

content 3
content 4
---
content 5
'''

# check metadata regex (we want metadata only, not content)

# Doesn't match correctly - not greedy enough
# \s Returns a match where the string contains a white space character
# \S Returns a match where the string DOES NOT contain a white space character

def extract_parts_1 (source):
    m = re.search(r'---\s([\s\S]*)\s---\s([\s\S]*)', source, re.MULTILINE)
    metadata = m.group(1)
    markdown = m.group(2)
    return metadata, markdown

def extract_meta (source):
    m = re.search(r'---([\s\w:]*[^-])---', source, re.MULTILINE)
    return m.group(1).strip()

def extract_parts_2 (source):
    m = re.search(r'---([\s\w:]*[^-])---([\s\S]*)', source, re.MULTILINE)
    metadata = m.group(1)
    markdown = m.group(2)
    return metadata.strip(), markdown.strip()


#meta,md = extract_parts_1(s)
#print(meta)

#meta = extract_meta(s)
#print(meta)

meta, md = extract_parts_2(s)
print(">{}<\n>{}<".format(meta, md))

s1 = "This is c a string"

m = re.search(r'\S*[^bc]*', s1)
print(m)
if m != None:
    print(m[0])

