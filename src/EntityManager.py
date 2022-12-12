import random as random
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
        for i in range(int(random()*30+50)):
            self.structureList.append(BerryBush(int(random()*10000)-5000), int(random()*10000)-5000)


    def checkRenderedEntities(self, playerObj):
        self.renderedStructureList = []
        self.renderedItemList = []
        self.renderedMobList = []

        for i in range(len(self.structureList)):
            if self.structureList[i].xCor == playerObj.mapXCor*100 + playerObj.inBlockXCor and self.structureList[i].yCor == playerObj.mapYCor * 100 + playerObj.inBlockYCor:
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
            if self.structureList[i].type() == BerryBush:
                self.structureList[i].growBerry(tickCount)

            if self.structureList[i].type() == Cave:
                self.structureList[i].spawnWolf(playerObj, self.renderedEntityList, win)

