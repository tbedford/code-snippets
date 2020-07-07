import urllib.parse

q = urllib.parse.quote_plus('Hey there!')
print(q)

q = urllib.parse.quote_plus('Hey, Punch & Judy?')
print(q)

q = urllib.parse.quote_plus('Hobbs + Shaw')
print(q)

