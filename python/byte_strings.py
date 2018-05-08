import sys

s1 = b'ABCDEFGH'

if (sys.version_info > (3, 0)):
    print ("Python version 3")
    for c in s1:
        print ("%d %c %c" % (c, c, c+32))
else:
    print ("Python version 2")
    for c in s1:
        n = ord(c)
        print ("%d %c %c" % (n, n, n+32))

        
