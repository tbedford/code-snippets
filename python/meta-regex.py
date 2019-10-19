# \s Returns a match where the string contains a white space character
# \S Returns a match where the string DOES NOT contain a white space character

import re

s1 = '''
---
slug: python-non-greedy-regexes
title: Python non-greedy regexes
summary: How to make Python regexes a little less greedy using the `?` modifier.
cat: Code
date_published: 2019-10-19
date_updated: 2019-10-19
---

# How to make Python regexes a little less greedy

There are these little things that once you learn about them you wonder how you ever did without them. The Python non-greedy modifier definitely falls into that category. I spent far t

Here was the problem:

```
---
title: This is some title
description: This is the description
---

Some content...
```

This is a simplified version of the metadata that each piece of content on the site has. What the code needs to do is extract the metadata and the content.

This seems straightforward. You might come up with:

```
---\s([\s\S]*)\s---\s([\s\S]*)
```

We can simplify that but getting rid of the extra new lines in our captured text by using the `.strip()` function in Python so you end up with:

```
---([\s\S]*)---([\s\S]*)
```

The metadata drops into the first `()` and the content into the second `()` and there are rainbows and unicorns and all is good in the world. Until this happens...

```
---
title: This is some title
description: This is the description
---

Some content...

Item | Description
--- | ---
A | A thing
B | Another thing

Some more content...
```

And now there are tears because it all goes horribly wrong. You see Python regexes are downright greedy. They try to match as much text as possible. Which means your regex now matches right down to the first `---` in the Markdown table. This is where you probably start trying all kinds of variations on your regex to restrict the match to only the metadata. But there's an easy little fix...

```
---([\s\S]*?)---([\s\S]*)
```

The secret is that addition of the `?` operator. Like many operators it has many functions but when it's next to `*` it means "don't be so darn greedy".

Here's the actual code where I use it:

``` python
def extract_parts(source):
    m = re.search(r'---([\s\S]*?)---([\s\S]*)', source, re.MULTILINE)
    metadata = m.group(1)
    markdown = m.group(2)
    return metadata.strip(), markdown.strip()
```

This little `?` turns out to be hellishly useful. For example:

``` html
<p>Para 1</p><p>Para 2></p>
```

If you only want the first para you could use `<p>.*?</p>`, and you'd only match the first para.

You can test this out with the following code:

``` python
import re

s = "<p>para 1</p><p>para 2</p>"

m = re.search(r'<p>.*</p>', s)
print(m.group(0))

m = re.search(r'<p>.*?</p>', s)
print(m.group(0))
```

Yes. Useful indeed. Once you know about the non-greedy operator you'll wonder how you ever did without it!

'''

# Greedy *? to for matched delimiters
def extract(source):
    m = re.search(r'---([\s\S]*?)---', source, re.MULTILINE)
    return m.group(1).strip()

print(extract(s1))
