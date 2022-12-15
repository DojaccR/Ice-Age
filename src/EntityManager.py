import random as Random
from Structure import *
from Item import *
from Entity import *
from HostileEntity import *
from Inventory import *


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

    def checkRenderedEntities(self, win):
        self.renderedStructureList = []
        self.renderedItemList = []
        self.renderedMobList = []

        for i in range(len(self.structureList)):

            if self.structureList[i].xCor <= win.get_width() and self.structureList[i].xCor >= -200 and self.structureList[i].yCor <= win.get_height() and self.structureList[i].yCor >= -200:
                self.renderedStructureList.append(self.structureList[i])

        for i in range(len(self.mobList)):
            if self.mobList[i].xCor <= win.get_width() and self.mobList[i].xCor >= 0 and self.mobList[i].yCor <= win.get_height() and self.mobList[i].yCor >= 0:
                self.renderedMobList.append(self.mobList[i])

        for i in range(len(self.itemList)):
            if self.itemList[i].xCor <= win.get_width() and self.itemList[i].xCor >= 0 and self.itemList[i].yCor <= win.get_height() and self.itemList[i].yCor >= 0:
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
                self.structureList[i].spawnWolf(playerObj,self.mobList, self.renderedMobList, win)

    def runMobFunctions(self, playerObj):
        for i in range(len(self.renderedMobList)):
            self.renderedMobList[i].die(self.mobList, self.itemList)
            self.renderedMobList[i].changeDir(e)
            self.renderedMobList[i].move(e)
            if isinstance(self.renderedMobList[i], HostileEntity):
                self.renderedMobList[i].target(playerObj)

    def runItemFunctions(self, playerObj, inventory, win):
        for i in range(len(self.renderedItemList)):
            self.renderedItemList[i].pickup(playerObj, inventory, self.itemList)

    def move(self, axis, direction, CAMERA_SPEED):

        if axis == "x" and direction == "positive":
            for i in range(len(self.structureList)):
                self.structureList[i].xCor += CAMERA_SPEED

            for i in range(len(self.mobList)):
                self.mobList[i].xCor += CAMERA_SPEED

            for i in range(len(self.renderedItemList)):
                self.itemList[i].xCor += CAMERA_SPEED

        if axis == "x" and direction == "negative":
            for i in range(len(self.structureList)):
                self.structureList[i].xCor -= CAMERA_SPEED

            for i in range(len(self.mobList)):
                self.mobList[i].xCor -= CAMERA_SPEED

            for i in range(len(self.itemList)):
                self.itemList[i].xCor -= CAMERA_SPEED

        if axis == "y" and direction == "positive":
            for i in range(len(self.structureList)):
                self.structureList[i].yCor += CAMERA_SPEED

            for i in range(len(self.mobList)):
                self.mobList[i].yCor += CAMERA_SPEED

            for i in range(len(self.itemList)):
                self.itemList[i].yCor += CAMERA_SPEED

        if axis == "y" and direction == "negative":
            for i in range(len(self.structureList)):
                self.structureList[i].yCor -= CAMERA_SPEED

            for i in range(len(self.mobList)):
                self.mobList[i].yCor -= CAMERA_SPEED

            for i in range(len(self.itemList)):
                self.itemList[i].yCor -= CAMERA_SPEED

    def playerInteract(self, playerObj, keys):
        if keys == "f":
            for i in range(len(self.renderedStructureList)):
                if int(sqrt((self.renderedStructureList[i].xCor-playerObj.xCor)**2+(self.renderedStructureList[i].yCor-playerObj.yCor)**2)) < 30 and type(self.renderedStructureList[i]) == BerryBush:
                    self.renderedStructureList[i].dropBerry(self.itemList)

        elif keys == "m1":
            print("mouse presssed")
            for i in range(len(self.renderedMobList)):
                if int(sqrt((self.renderedMobList[i].xCor-playerObj.xCor)**2+(self.renderedMobList[i].yCor-playerObj.yCor)**2)) < 30:
                    self.renderedMobList[i].health -= 1
