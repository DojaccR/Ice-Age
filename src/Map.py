import os
import random as r
import pygame


class Map:
    mapID = 0
    mapSize = 100
    mapFile = ""
    mapTiles = []
    renderedTiles = [[]]
    tileWidth = 0
    tileHeight = 0
    tileTexturePath = ["assets/Grass0.png", "assets/Grass1.png", "assets/Sand.png"]
    tileTextures = []

    def __init__(self, mapID):
        for i in range(len(self.tileTexturePath)):
            self.tileTextures.append(pygame.image.load(self.tileTexturePath[i]))

        self.tileWidth = self.tileTextures[0].get_width()
        self.tileHeight = self.tileTextures[0].get_height()

        if str(mapID) == "create":
            self.generate()
            map = open("maps/map1.txt")
            for i in range(100):
                mapStr = map.readline()
                mapChars = list()
                mapChars.extend(mapStr)
                self.mapTiles.append(mapChars)
        else:
            map = open("maps/map1.txt")
            for i in range(100):
                mapStr = map.readline()
                mapChars = list()
                mapChars.extend(mapStr)
                self.mapTiles.append(mapChars)


    #calculates and directly displays whats on screen
    def render1(self, playerObj, win):
        for i in range(int((win.get_width()/self.tileWidth)+2)):
            #print(i)
            for j in range((int(win.get_height()/(self.tileHeight/2))+3)):
                if (playerObj.mapYCor-int(((win.get_height()/self.tileHeight)+1)/2)+j) % 2 == 0:
                    win.blit(self.tileTextures[int(self.mapTiles[playerObj.mapXCor-int(((win.get_width()/self.tileWidth)+1)/2)+i][playerObj.mapYCor-int(((win.get_height()/self.tileHeight)+1)/2)+j])], (self.tileWidth * i + playerObj.inBlockXCor - self.tileWidth, self.tileHeight / 2 * j + playerObj.inBlockYCor - self.tileHeight * 3 / 2))
                else:
                    win.blit(self.tileTextures[int(self.mapTiles[playerObj.mapXCor-int(((win.get_width()/self.tileWidth)+1)/2)+i][playerObj.mapYCor-int(((win.get_height()/self.tileHeight)+1)/2)+j])], (self.tileWidth * i + playerObj.inBlockXCor - self.tileWidth / 2 * 3, self.tileHeight / 2 * j + playerObj.inBlockYCor - self.tileHeight * 3 / 2))

    def checkAdjacent(self, cor, mapSize, nextList, changed, chance):
        if cor[0] > 0 and r.random() * 100 < chance:
            if changed.count([cor[0] - 1, cor[1]]) == 0 and nextList.count([cor[0] - 1, cor[1]]) == 0:
                nextList.append([cor[0] - 1, cor[1]])

        if cor[0] < mapSize - 1 and r.random() * 100 < chance:
            if changed.count([cor[0] + 1, cor[1]]) == 0 and nextList.count([cor[0] + 1, cor[1]]) == 0:
                nextList.append([cor[0] + 1, cor[1]])

        if cor[1] > 0 and r.random() * 100 < chance:
            if changed.count([cor[0], cor[1] - 1]) == 0 and nextList.count([cor[0], cor[1] - 1]) == 0:
                nextList.append([cor[0], cor[1] - 1])

        if cor[1] < mapSize - 1 and r.random() * 100 < chance:
            if changed.count([cor[0], cor[1] + 1]) == 0 and nextList.count([cor[0], cor[1] + 1]) == 0:
                nextList.append([cor[0], cor[1] + 1])

    def grow(self, corList, blockType, mapBlocks):
        for i in range(len(corList) - 1):
            mapBlocks[corList[i][0]][corList[i][1]] = blockType

    def generateBiome(self, mapBlocks):
        chance = 100
        decay = 0.95
        biome = int(r.random() * 2) + 1

        startCor = [int(r.random() * 100), int(r.random() * 100)]

        corList = [startCor]
        changed = []
        nextList = []
        for i in range(30):
            self.grow(corList, biome, mapBlocks)
            length = len(corList)
            for i in range(length):
                self.checkAdjacent(corList[0], 100, nextList, changed, chance)
                changed.append(corList.pop(0))
            corList = nextList
            chance = chance * decay
    def generate(self):
        map = open("maps/map1.txt", "w")
        mapBlocks = []

        x = ""

        for i in range(100):
            mapBlocks.append([])
            for j in range(100):
                mapBlocks[i].append(0)

        for i in range(20):
            self.generateBiome(mapBlocks)

        for i in range(100):
            for j in range(100):
                x += str(mapBlocks[i][j])

            x += "\n"
        map.write(x)

    def getAdjacent(self, direction, xCor, yCor):
        if direction == "up":
            return str(xCor + "," + (yCor - 1))
        elif direction == "down":
            return str(xCor + "," + (yCor + 1))
        elif direction == "left":
            return str((xCor - 1) + "," + yCor)
        elif direction == "right":
            return str((xCor + 1) + "," + yCor)
        else:
            print("invalid")
            return "invalid"

    def blockChange(self, playerObj):
        if playerObj.inBlockXCor > self.tileWidth:
            playerObj.mapXCor -= 1
            playerObj.inBlockXCor = 1

        if playerObj.inBlockXCor < 0:
            playerObj.mapXCor += 1
            playerObj.inBlockXCor = self.tileWidth - (self.tileWidth/10) + 1

        if playerObj.inBlockYCor > self.tileHeight/2:
            playerObj.mapYCor -= 1
            playerObj.inBlockYCor = 1

        if playerObj.inBlockYCor < 0:
            playerObj.mapYCor += 1
            playerObj.inBlockYCor = self.tileHeight/2 - (self.tileWidth/10) + 1

