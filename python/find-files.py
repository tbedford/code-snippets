import os

def find_files(root):
    md_files = []
    for root, dirs, files in os.walk(root):
        for f in files:
            if f.endswith(".md"):
                md_files.append(os.path.join(root, f))
    return md_files

root = "/Users/abedford/site/thedatamangler"
print(find_files(root))
