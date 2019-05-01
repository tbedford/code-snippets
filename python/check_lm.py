#!/usr/bin/env python3
from os.path import abspath
from os.path import getmtime

f = open ('lm.txt', 'r')

for line in f:
    # chomp line
    line = line.strip('\n')
    filename, file_lm = line.split(':')
    file_lm = int(file_lm)
    lm = int(getmtime(filename))
    if lm > file_lm:
        print("Updated: %s: was: %s now: %s" % (filename, file_lm, lm))
