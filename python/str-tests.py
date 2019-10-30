t = "https://tonys-notebook.com"
s1 = "http"
s2 = "/blahblah"
s3 = "./foobar"

def normalize(base, link):

    if link.startswith('http'):
        return link
    
    if link.startswith('/'):
        return base + link

    if link.startswith('./'):
        return base + link[1:]

print(normalize(t, t))
print(normalize(t, s1))
print(normalize(t, s2))
print(normalize(t, s3))




