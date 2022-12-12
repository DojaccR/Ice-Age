import random as Random
from Structure import *
from Item import *
from Entity import *


class EntityManager:
    mobList = []
    structureList = []
    itemList = []

    renderedStructureList = []
    renderedMobList = []
    renderedItemList = []

    def __init__(self):
        for i in range(10):
            xCor = (int(Random.random() * 1280))
            yCor = (int(Random.random() * 720))
            print("Berry Bush at: " + str(xCor) + " " + str(yCor))
            self.structureList.append(BerryBush(xCor, yCor))

        for i in range(int(Random.random()*30+300)):
            xCor = (int(Random.random() * 10000) - 5000)
            yCor = (int(Random.random() * 10000) - 5000)
            print("Berry Bush at: " + str(xCor) + " " + str(yCor))
            self.structureList.append(BerryBush(xCor, yCor))

        for i in range(int(Random.random() * 5 + 50)):
            print("Cave at: " + str(xCor) + " " + str(yCor))
            xCor = (int(Random.random() * 10000) - 5000)
            yCor = (int(Random.random() * 10000) - 5000)
            self.structureList.append(Cave(xCor, yCor))


    def checkRenderedEntities(self, playerObj, win):
        self.renderedStructureList = []
        self.renderedItemList = []
        self.renderedMobList = []

        for i in range(len(self.structureList)):
            if self.structureList[i].xCor <= playerObj.mapXCor*100 + playerObj.inBlockXCor and self.structureList[i].yCor <= playerObj.mapYCor * 100 + playerObj.inBlockYCor:
                self.renderedStructureList.append(self.structureList[i])

        for i in range(len(self.mobList)):
            if self.mobList[i].xCor == playerObj.mapXCor * 100 + playerObj.inBlockXCor and self.mobList[i].yCor == playerObj.mapYCor * 100 + playerObj.inBlockYCor:
                self.renderedMobList.append(self.mobList[i])

        for i in range(len(self.itemList)):
            if self.itemList[i].xCor == playerObj.mapXCor * 100 + playerObj.inBlockXCor and self.itemList[i].yCor == playerObj.mapYCor * 100 + playerObj.inBlockYCor:
                self.renderedItemList.append(self.itemList[i])

    def renderEntities(self, win):
        for i in range(len(self.renderedStructureList)):
            self.renderedStructureList[i].render(win)

        for i in range(len(self.renderedMobList)):
            self.renderedMobList[i].render(win)

        for i in range(len(self.renderedItemList)):
            self.renderedItemList[i].render(win)

    def runStructureFunctions(self, tickCount, playerObj, win):
        for i in range(len(self.structureList)):
            if type(self.structureList[i]) == BerryBush:
                self.structureList[i].growBerry(tickCount)

            if type(self.structureList[i]) == Cave:
                self.structureList[i].spawnWolf(playerObj, self.renderedMobList, win)

    def move(self, axis, direction, CAMERA_SPEED):
        if axis == "x" and direction == "positive":
            for i in range(len(self.renderedStructureList)):
                self.renderedStructureList[i].xCor += CAMERA_SPEED

            for i in range(len(self.renderedMobList)):
                self.renderedMobList[i].xCor += CAMERA_SPEED

            for i in range(len(self.renderedItemList)):
                self.renderedItemList[i].xCor += CAMERA_SPEED

        if axis == "x" and direction == "negative":
            for i in range(len(self.renderedStructureList)):
                self.renderedStructureList[i].xCor -= CAMERA_SPEED

            for i in range(len(self.renderedMobList)):
                self.renderedMobList[i].xCor -= CAMERA_SPEED

            for i in range(len(self.renderedItemList)):
                self.renderedItemList[i].xCor -= CAMERA_SPEED

        if axis == "y" and direction == "positive":
            for i in range(len(self.renderedStructureList)):
                self.renderedStructureList[i].yCor += CAMERA_SPEED

            for i in range(len(self.renderedMobList)):
                self.renderedMobList[i].yCor += CAMERA_SPEED

            for i in range(len(self.renderedItemList)):
                self.renderedItemList[i].yCor += CAMERA_SPEED


        if axis == "y" and direction == "negative":
            for i in range(len(self.renderedStructureList)):
                self.renderedStructureList[i].yCor -= CAMERA_SPEED

            for i in range(len(self.renderedMobList)):
                self.renderedMobList[i].yCor -= CAMERA_SPEED

            for i in range(len(self.renderedItemList)):
                self.renderedItemList[i].yCor -= CAMERA_SPEED

