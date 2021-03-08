global_cats = []

def read_file(filename):
    f = open(filename, mode='r', encoding='utf-8')
    source = f.read()
    f.close()
    return source

def load_cats(catfile):
    print('Loading cats from: ', catfile)
    src = read_file(catfile)
    lines = src.splitlines()
    for line in lines:
        name, desc, image = line.split('|', 2)
        cat_obj = {}
        cat_obj['name'] = name.strip()
        cat_obj['desc'] = desc.strip()
        cat_obj['image'] = image.strip()
        global_cats.append(cat_obj)
    return

load_cats('./cats.txt')
print(global_cats)
