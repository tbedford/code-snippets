import re

s1 = "  This! is a? title to slugify?! "
print(s1)

def slugify(title):
    title = title.strip().lower().replace(' ', '_')
    title = re.sub(r'\W', '', title)
    title = title.replace('_', '-')
    return title
    
print(">{slug}<".format(slug=slugify(s1)))

