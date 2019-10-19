import re

s = "<p>para 1</p><p>para 2</p>"

m = re.search(r'<p>.*?</p>', s)
print(m.group(0))

m = re.search(r'<p>.*</p>', s)
print(m.group(0))
