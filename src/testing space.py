import os
import random as r

map = open("maps/map1.txt", "w")
mapBlocks = []


x = ""

for i in range(100):
    mapBlocks.append([])
    for j in range(100):
        mapBlocks[i].append(0)



def checkAdjacent(cor, mapSize, nextList, changed, chance):
    if cor[0] > 0 and r.random() * 100 < chance:
        if changed.count([cor[0] - 1, cor[1]]) == 0 and nextList.count([cor[0] - 1, cor[1]]) == 0:
            nextList.append([cor[0] - 1, cor[1]])
            print("appended")

    if cor[0] < mapSize - 1 and r.random() * 100 < chance:
        if changed.count([cor[0] + 1, cor[1]]) == 0 and nextList.count([cor[0] + 1, cor[1]]) == 0:
            nextList.append([cor[0] + 1, cor[1]])
            print("appended")

    if cor[1] > 0 and r.random() * 100 < chance:
        if changed.count([cor[0], cor[1] - 1]) == 0 and nextList.count([cor[0], cor[1] - 1]) == 0:
            nextList.append([cor[0], cor[1] - 1])
            print("appended")

    if cor[1] < mapSize - 1 and r.random() * 100 < chance:
        if changed.count([cor[0], cor[1] + 1]) == 0 and nextList.count([cor[0], cor[1] + 1]) == 0:
            nextList.append([cor[0], cor[1] + 1])
            print("appended")

def grow(corList, blockType, mapBlocks):
    for i in range(len(corList)-1):
        print(i)
        print(len(corList)-1)
        mapBlocks[corList[i][0]][corList[i][1]] = blockType


def generateBiome():
    chance = 100
    decay = 0.95
    biome = int(r.random() * 2) + 1

    startCor = [int(r.random() * 100), int(r.random() * 100)]

    corList = [startCor]
    changed = []
    nextList = []
    for i in range(30):
        print("round" + str(i) + str(len(corList)))
        grow(corList, biome, mapBlocks)
        length = len(corList)
        for i in range(length):
            print("looping" + str(len(corList)))

            checkAdjacent(corList[0], 100, nextList, changed, chance)
            changed.append(corList.pop(0))
        print("new " + str(len(nextList)))
        corList = nextList
        chance = chance * decay

for i in range(20):
    generateBiome()

for i in range(100):
    for j in range(100):
        x += str(mapBlocks[i][j])

    x += "\n"
print(x)
map.write(x)




