import os


def load_file(filebase, exts):
    for ext in exts:
        fn = filebase + '.' + ext
        print('Checking for ', fn)
        if os.path.exists(fn):
            print('Found!')
            break

filebase = 'index'
exts = ['md', 'yml', 'txt']

load_file(filebase, exts)

