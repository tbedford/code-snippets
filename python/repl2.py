import re

source = '''This is
some https://support.ably.com/solution/articles/3000030054-what-is-an-app-api-key
kjkj
and even more https://support.ably.com/, some https://knowledge.ably.com/solution/articles/3000030054-what-is-an-app-api-key https://knowledge.ably.com/123-hello-world-1 xfhfhgf
and text
this is https://knowledge.ably.com/123-hello-world-1'
this is https://knowledge.ably.com/123-hello-world-2'
this is https://knowledge.ably.com/123-hello-world-1* '
text
'''

link = r'(https://knowledge.ably.com/\S*)-1'
x, n = re.subn(link, r'\1', source, re.MULTILINE)
print(x)
print(n)


