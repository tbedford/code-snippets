# simple hash - sum of ASCII values Add up the ASCII values of all
# characters in the string and return the sum as the hash value.

def simple_hash(s):
    return sum(ord(c) for c in s)

print(simple_hash("hello"))


p = "hello"

for c in p:
    print(c)
    print(ord(c))

print('sum: --> ', sum([1,2,3]))
