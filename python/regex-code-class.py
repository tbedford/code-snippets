import re

mkdown = '''
``` python
application_id = "your_application_id"

payload = {
    'application_id': application_id,
    'iat': int(time.time()),
    'jti': str(uuid4()),
}
```

AAA text

``` json
{
"name": "Fred"
}
```

BBB text.
'''

def read_file(filename):
    f = open (filename, mode='r', encoding='utf-8')
    source = f.read()
    f.close()
    return source

mkdown1 = read_file("understanding-jwts.md")

# Get code block classes e.g. python, shell
classes = re.findall(r'```\s?(\w+)\s', mkdown1)

print(classes)
