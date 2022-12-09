import os
import random as r
import pygame


class Map:
    mapID = 0
    mapFile = ""
    mapTiles = []
    renderedTiles = [[]]

    def __init__(self, mapID):
        if str(mapID) == "create":
            map = open("map1.txt", "w")
        else:
            map = open("map1.txt")
            for i in range(100):
                mapStr = map.readline()
                mapChars = list()
                mapChars.extend(mapStr)
                self.mapTiles.append(mapChars)


    #calculates and directly displays whats on screen
    def render1(self, playerObj, win):

        #print(len(self.mapTiles))
        #print(len(self.mapTiles[0]))
        print("rendering " + str((int(win.get_height()/100)+1)*(int((win.get_width()/100)+1))) + " chunks")
        for i in range(int((win.get_width()/100)+1)):
            #print(i)
            for j in range((int(win.get_height()/100)+1)):
                #print(j)
                if int(self.mapTiles[playerObj.mapXCor-int(((win.get_width()/100)+1)/2)+i][playerObj.mapYCor-int(((win.get_height()/100)+1)/2)+j]) == 1:
                    #print(playerObj.mapXCor - int(((win.get_width() / 50) + 1) / 2) + i)
                    #print(playerObj.mapYCor - int(((win.get_height() / 50) + 1) / 2) + j)
                    win.blit(pygame.image.load("assets/Grass.png"), (100*i, 100*j))
                else:
                    #print(playerObj.mapXCor - int(((win.get_width() / 50) + 1) / 2) + i)
                    #print(playerObj.mapYCor - int(((win.get_height() / 50) + 1) / 2) + j)
                    win.blit(pygame.image.load("assets/Grass2.png"), (100*i, 100*j))


    #loads on screen into array and then displayed
    def render2(self, playerObj, win):
        for i in range(int((win.get_width / 50) + 1)):
            for j in range((int(win.get_height / 50) + 1)):
                self.renderedTiles[i][j] = self.mapTiles[playerObj.mapXCor - int(((win.get_width / 50) + 1) / 2) + i][
                    playerObj.mapYCor - int(((win.get_height / 50) + 1) / 2) + j]


    #loads whole map
    def render3(self, playerObj, win):
        for i in range(100):
            for j in range(100):
                if int(self.mapTiles[i][j]) == 1:
                    win.blit(pygame.image.load("assets/Grass.png"), (50*i, 50*j))
                else:
                    win.blit(pygame.image.load("assets/Grass2.png"), (50*i, 50*j))

    def generate(self):
        map = open("map1.txt", "w")

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

