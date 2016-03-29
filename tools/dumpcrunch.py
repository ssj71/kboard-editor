#!/usr/bin/env python3

import fileinput

n = 0
for line in fileinput.input():
    w = line.split()
    if(len(w) == 0):
        continue
    if(w[0].startswith("00") and w[0].isdigit()):
        if(int(w[0]) == 0):
            print()
            print(n, " (",fileinput.lineno(), ")")
        elif(int(w[0]) == 10):
            print(line[39:53] )
        elif(int(w[0]) > 0):
            print(line[6:53] )
    elif(w[0].isdigit()):
        n = int(w[0])

