
# Wasteful HTML spacing

s = '''
 <html>
     <head>
    <title>This is the title</title>
  </head>
    <body>
           <p>Hello</p>
   </body>
   </html>
'''

def minify (html):
    longline = ""
    lines = html.splitlines()
    for line in lines:
        line = line.strip()
        longline = longline + line 
    return longline

print(minify(s))


