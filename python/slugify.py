import re

s1 = "  This! is a? title to slugify?! "
print(s1)


# Slight hack is to convert spaces to underscore first.  This allows
# you just use '\W' to remove unwanted chars from string. You then
# need to convert the underscores to '-'.
def slugify(title):
    title = title.strip().lower().replace(' ', '_')
    title = re.sub(r'\W', '', title)
    title = title.replace('_', '-')
    return title
    
print(">{slug}<".format(slug=slugify(s1)))

