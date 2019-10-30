#!/usr/bin/env python3
import time

filename = "test.log"
with open(filename, "a") as fout:
    n = 0
    while True:
        fout.write("Event stuff: " + str(n) + "\n")
        fout.flush()
        n = n + 1
        time.sleep(3)



