str= ' this | is | a string  '

s1, s2, s3 = str.split('|', 2)

print('>%s<' % s1.strip())
print('>%s<' % s2)
print('>%s<' % s3)


s = str.split('|', 2)
print(s)
