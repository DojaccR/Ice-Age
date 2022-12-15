import os
import random as r
import pygame


class Map:
    mapID = 0
    mapFile = ""
    mapTiles = []
    renderedTiles = [[]]
    tileWidth = 0
    tileHeight = 0
    tileTexturePath = ["assets/Grass0.png", "assets/Grass1.png"]
    tileTextures = []

    def __init__(self, mapID):
        for i in range(len(self.tileTexturePath)):
            self.tileTextures.append(pygame.image.load(self.tileTexturePath[i]))

        self.tileWidth = self.tileTextures[0].get_width()
        self.tileHeight = self.tileTextures[0].get_height()

        if str(mapID) == "create":
            self.generate()
        else:
            map = open("map1.txt")
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

    def generate(self):
        map = open("map1.txt", "w")
        w, h = 8, 5
        Matrix = [[None for x in range(w)] for y in range(h)]
        x = ""

        for i in range(100):
            for j in range(100):
                if int(r.random() * 2) == 1:
                    x += "0"
                else:
                    x += "1"

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
        #print(str(playerObj.inBlockXCor) + " " + str(playerObj.inBlockYCor))
        if playerObj.inBlockXCor > self.tileWidth:
            playerObj.mapXCor -= 1
            #print(playerObj.mapXCor)
            playerObj.inBlockXCor = 1

        if playerObj.inBlockXCor < 0:
            playerObj.mapXCor += 1
            #print(playerObj.mapXCor)
            playerObj.inBlockXCor = self.tileWidth - (self.tileWidth/10) + 1

        if playerObj.inBlockYCor > self.tileHeight/2:
            playerObj.mapYCor -= 1
            #print(playerObj.mapYCor)
            playerObj.inBlockYCor = 1

        if playerObj.inBlockYCor < 0:
            playerObj.mapYCor += 1
            #print(playerObj.mapYCor)
            playerObj.inBlockYCor = self.tileHeight/2 - (self.tileWidth/10) + 1

