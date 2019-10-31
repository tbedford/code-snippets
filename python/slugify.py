# Generate a slug

s1 = "  This is a title to slugify "
print(s1)

def slugify(title):
    return title.strip().lower().replace(' ', '-')
    
print(">{slug}<".format(slug=slugify(s1)))

