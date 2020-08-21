import base64

# Base64 encodes binary info as ASCII string

fn1 = "timmy.jpg"
fn2 = "test.jp"

# Open test file as input in binary mode and read in bytes
f = open (fn1, "rb")
bytes = f.read()
f.close()

# Encode the picture as Base64 string
e = base64.b64encode(bytes)

# print(e)

# decode the string into bytes
d = base64.b64decode(e)

# Write decoded bytes to test file 
f = open (fn2, "wb")
f.write(d)
f.close()
# Make sure you check the test file now displays correctly

