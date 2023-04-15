import numpy as np
import random as r
import pygame


class Map:


    def __init__(self, mapID):
        self.mapID = 0
        self.mapSize = 1000
        self.mapFile = ""
        self.mapTiles = []
        self.renderedTiles = [[]]
        self.tileWidth = 0
        self.tileHeight = 0
        self.tileTexturePath = ["assets/Grass0.png", "assets/Grass1.png", "assets/Sand.png", "assets/Water0.png",
                           "assets/water1.png"]
        self.waterTexturePath = ["assets/Water0.png", "assets/water1.png"]
        self.tileTextures = []

        for i in range(len(self.tileTexturePath)):
            self.tileTextures.append(pygame.image.load(self.tileTexturePath[i]))

        self.tileWidth = self.tileTextures[0].get_width()
        self.tileHeight = self.tileTextures[0].get_height()

        if str(mapID) == "create":
            self.generate()
            map = open("maps/map1.txt")
            for i in range(self.mapSize):
                mapStr = map.readline()
                mapChars = list()
                mapChars.extend(mapStr)
                self.mapTiles.append(mapChars)
        else:
            map = open("maps/map1.txt")
            for i in range(self.mapSize):
                mapStr = map.readline()
                mapChars = list()
                mapChars.extend(mapStr)
                self.mapTiles.append(mapChars)

    # Renders the map to screen by drawing all visible tiles from top left to bottom right
    def render1(self, playerObj, win):
        for i in range(int((win.get_width()/self.tileWidth)+2)):
            for j in range((int(win.get_height()/(self.tileHeight/2))+3)):
                if (playerObj.mapYCor-int(((win.get_height()/self.tileHeight)+1)/2)+j) % 2 == 0:
                    win.blit(self.tileTextures[int(self.mapTiles[int(playerObj.mapXCor-int(((win.get_width()/self.tileWidth)+1)/2)+i)][int(playerObj.mapYCor-int(((win.get_height()/self.tileHeight)+1)/2)+j)])], (self.tileWidth * i + playerObj.inBlockXCor - self.tileWidth, self.tileHeight / 2 * j + playerObj.inBlockYCor - self.tileHeight * 3 / 2))
                else:
                    win.blit(self.tileTextures[int(self.mapTiles[int(playerObj.mapXCor-int(((win.get_width()/self.tileWidth)+1)/2)+i)][int(playerObj.mapYCor-int(((win.get_height()/self.tileHeight)+1)/2)+j)])], (self.tileWidth * i + playerObj.inBlockXCor - self.tileWidth / 2 * 3, self.tileHeight / 2 * j + playerObj.inBlockYCor - self.tileHeight * 3 / 2))

    # Adds adjacent blocks to next blocks to fill i.e. nextList given the chance of spreading.
    def addAdjacent(self, cor, mapSize, nextList, changed, chance):
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

    # Generates biomes using the lazy flood fill algorithm
    def generateBiome(self, mapBlocks):
        chance = 100
        decay = 0.98
        biome = int(r.random() * 2) + 1
        print(biome)

        startCor = [int(r.random() * self.mapSize), int(r.random() * self.mapSize)]

        corList = [startCor]
        changed = []
        nextList = []
        for i in range(90):
            self.grow(corList, biome, mapBlocks)
            print("grown: " + str(i))
            length = len(corList)
            for i in range(length):
                self.addAdjacent(corList[0], self.mapSize, nextList, changed, chance)
                changed.append(corList.pop(0))
            corList = nextList
            chance = chance * decay

    def generateRiver(self, mapBlocks):
        pass

    # Generates the map
    def generate(self):
        map = open("maps/map1.txt", "w")
        mapBlocks = np.zeros((self.mapSize, self.mapSize), dtype=int)

        x = ""

        for i in range(20):
            self.generateBiome(mapBlocks)

        for i in range(self.mapSize):
            for j in range(self.mapSize):
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

    # two coordinate systems are used. The map(X/Y)Cor describes the grid and inBlock(X/Y)Cor describes the position of
    # the player within the block of the grid of the map.
    # The below function checks if the player moves from one grid block to another grid block.
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

