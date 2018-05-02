# Encode an entry in XML
#<entry>
#  <title>Creating an Atom feed</title>
#  <link href="https://coffeeandcode.neocities.org/creating-atom-feed.html"/>
#  <id>urn:uuid:2E4A626F-FF02-47F0-9538-254F76F5C7EF</id>
#  <updated>2017-11-10T11:07:29+0000</updated>
#  <published>2017-11-10T11:07:29+0000</published>
#  <summary>This is a summary of the article.</summary>
#</entry>

base_url = "https://coffeeandcode.neocities.org/"

template = '''
<entry>
  <title>%s</title>
  <link href="%s%s"/>
  <id>%s</id>
  <updated>%s</updated>
  <published>%s</published>
  <summary>%s</summary>
</entry>
'''

test = '''
<summary>%s</summary>
'''

test2 = '''
<link href="%s%s"/>
'''

test3 = '''
<summary>%s</summary>
<link href="%s%s"/>
'''

filename = "test.html"
summary = "This is a summary"

def fn_test3(filename, summary):

    return (test3 % (summary, base_url, filename))

print(fn_test3(filename, summary))


