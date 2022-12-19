import os
import random as r

map = open("map1.txt", "w")
mapBlocks = []
chance = 100
decay = 0.95

x = ""

for i in range(100):
    mapBlocks.append([])
    for j in range(100):
        mapBlocks[j].append([0])

startCor = [r.random()*100, r.random()*100]

corList = [startCor]

while len(corList) > 0:


map.write(x)

def checkAdjacent(cor, mapSize, mapBlocks):
