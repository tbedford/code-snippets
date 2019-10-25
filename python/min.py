# 1. Wasteful HTML spacing
# 2. Remove line comments (not from code blocks)

def do_backslash_markers(t):
    s1 = r"\\"
    s2 = r"__BACKSLASH__"
    return re.sub (s1, s2, t, 0)

import re

s = '''
 <html>
     <head>
      <!-- this is a loooooonnnnggg comment and we don't need it   -->
    <title>This is the title</title>
  </head>
    <body>
           <p>Hello</p>

<code>
   &lt;!-- this is another comment in a code block --&gt;
        don't remove space here
</code>

<pre>
     Pre formatted text
</pre>

   </body>
   </html>
'''

# we need a simple way to pull out all code blocks and pre and then
# put them back!

def minify (html):
    longline = ""
    lines = html.splitlines()
    for line in lines:
        line = re.sub(r'<!--[\s\S]*?-->', '', line)
        line = line.strip()
        longline = longline + line 
    return longline

print(minify(s))


