#!/usr/bin/env python3
from os.path import abspath
from os.path import getmtime
import fileinput

for line in fileinput.input():
    #print(line)
    # chomp line
    line = line.strip('\n')
    print("%s: %s" % (abspath(line), int(getmtime(line))) )
