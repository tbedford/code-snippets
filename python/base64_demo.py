import base64

# Base64 encodes binary info as ASCII string

fn = "timmy.jpg"

# How to read and write a binary file

f = open (fn, "rb")
bytes = f.read()
f.close()

f = open ("test.jpg", "wb")
f.write(bytes)
f.close()

f = open (fn, "rb")
bytes = f.read()
f.close()

e = base64.b64encode(bytes)

# print(e)

d = base64.b64decode(e)

f = open ("test.jpg", "wb")
f.write(d)
f.close()


