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
            for line in map:
                mapStr = map.readline()
                mapChars = list()
                mapChars.extend(mapStr)
                self.mapTiles.append(mapChars)
    
    def render1(self, playerObj, win):
        print(playerObj.mapXCor-int(((win.get_width()/50)+1)/2)+0)
        print(playerObj.mapYCor-int(((win.get_height()/50)+1)/2)+0)
        print(len(self.mapTiles))
        for i in range(int((win.get_width()/50)+1)):
            print(i)
            for j in range((int(win.get_height()/50)+1)):
                print(j)
                if self.mapTiles[playerObj.mapXCor-int(((win.get_width()/50)+1)/2)+i][playerObj.mapYCor-int(((win.get_height()/50)+1)/2)+j] == 1:
                    win.blit(pygame.image.load("assets/Grass.png"), (50*i, 50*j))
                else:
                    win.blit(pygame.image.load("assets/Grass2.png"), (50*i, 50*j))

    def render2(self, playerObj, win):
        for i in range(int((win.get_width / 50) + 1)):
            for j in range((int(win.get_height / 50) + 1)):
                self.renderedTiles[i][j] = self.mapTiles[playerObj.mapXCor - int(((win.get_width / 50) + 1) / 2) + i][
                    playerObj.mapYCor - int(((win.get_height / 50) + 1) / 2) + j]

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


