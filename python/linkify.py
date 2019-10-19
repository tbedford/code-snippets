# Linkify cat
def cat_link(cat):
    cat_link = '<a href="./index-' + cat + '">' + cat + '</a>'
    print(cat_link)

cat_link("Books")
