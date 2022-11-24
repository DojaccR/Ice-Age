import os
import random as r

map = open("map1.txt", "w")

x = ""

for i in range(10):
    for j in range(10):
        if int(r.random()*2) == 1:
            x+="0"
        else:
            x+="1"

    x+="\n"

map.write(x)