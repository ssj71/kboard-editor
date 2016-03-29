#!/usr/bin/env python3

import fileinput

#this takes the crunched file and separates it (starting at message number n) into each individual dump so you can diff them
n = 59
f = open("separated/"+str(n),'w')
for line in fileinput.input():
    w = line.split()
    if(len(w) == 0):
        continue
    if(w[0].isdigit()):
        i = int(w[0])
        if(i == n): 
            f.close()
            f = open("separated/"+str(n),"w")
            n+=12
        if(i>255):
            continue
    f.write(line)
f.close()
