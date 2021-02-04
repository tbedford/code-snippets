import re

source = '''This is
some https://support.ably.com/solution/articles/3000030054-what-is-an-app-api-key
and even more https://support.ably.com/, some https://support.ably.com/solution/articles/3000030054-what-is-an-app-api-key
and text
 https://support.ably.com/solution/articles/new?folder_id=3000009, the
here https://support.ably.com/123.
and even more https://support.ably.com/.
 https://support.ably.com/solution/articles/new?folder_id=3000009
https://support.ably.com/123-hello-world. 34
https://support.ably.com/123-hello-world, 12
**https://support.ably.com/123-hello-world** hi
this is (https://support.ably.com/123-hello-world) hi
this is https://support.ably.com/123-hello-world<br/> hi
this is https://support.ably.com/123-hello-world:
this is https://support.ably.com/123-hello-world'
text
'''

# Link type 1
regex = r'([\s.,*<:)"\'])'
link1 = '(https://support.ably.com/)' + regex
link2 = "https://knowledge.ably.com/"
x = re.sub(link1, link2 + r'\2', source, re.MULTILINE)

# Link type 2
s = re.escape('https://support.ably.com/solution/articles/new?folder_id=3000009')
link1 = '(' + s + ')' + regex
link2 = "https://knowledge.ably.com/"
y = re.sub(link1, link2 + r'\2', source, re.MULTILINE)

# Link type 3
s = re.escape('https://support.ably.com/123-hello-world')
link1 = '(' + s + ')' + regex
link2 = "https://knowledge.ably.com/"
y = re.sub(link1, link2 + r'\2', source, re.MULTILINE)

print(y)

