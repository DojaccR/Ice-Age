import random as Random
import Structure
import HostileEntity
import math
import PeacefulEntity


class EntityManager:
    mobList = []
    structureList = []
    itemList = []

    renderedStructureList = []
    renderedMobList = []
    renderedItemList = []

    renderedDestructableStructureList = []

    def __init__(self):
        # generates initial entities on the map

        # adds berry bushes
        for i in range(int(Random.random()*30+300)):
            xCor = (int(Random.random() * 10000) - 5000)
            yCor = (int(Random.random() * 10000) - 5000)
            self.structureList.append(Structure.BerryBush(xCor, yCor))

        # adds caves
        for i in range(int(Random.random() * 5 + 50)):
            xCor = (int(Random.random() * 10000) - 5000)
            yCor = (int(Random.random() * 10000) - 5000)
            self.structureList.append(Structure.Cave(xCor, yCor))

        # spawns mammoths
        for i in range(int(Random.random()*30+300)):
            xCor = (int(Random.random() * 10000) - 5000)
            yCor = (int(Random.random() * 10000) - 5000)
            self.mobList.append(PeacefulEntity.Mammoth(len(self.mobList), xCor, yCor))

    # Checks which entities are on screen
    def checkRenderedEntities(self, win):
        self.renderedStructureList = []
        self.renderedItemList = []
        self.renderedMobList = []
        self.renderedDestructableStructureList = []

        for i in range(len(self.structureList)):

            if self.structureList[i].xCor <= win.get_width() and self.structureList[i].xCor >= -200 and self.structureList[i].yCor <= win.get_height() and self.structureList[i].yCor >= -200:
                self.renderedStructureList.append(self.structureList[i])
                if isinstance(self.structureList[i], Structure.DestructableStructure):
                    self.renderedDestructableStructureList.append(self.structureList[i])

        for i in range(len(self.mobList)):
            if self.mobList[i].xCor <= win.get_width() and self.mobList[i].xCor >= -200 and self.mobList[i].yCor <= win.get_height() and self.mobList[i].yCor >= -200:
                self.renderedMobList.append(self.mobList[i])

        for i in range(len(self.itemList)):
            if self.itemList[i].xCor <= win.get_width() and self.itemList[i].xCor >= -20 and self.itemList[i].yCor <= win.get_height() and self.itemList[i].yCor >= -20:
                self.renderedItemList.append(self.itemList[i])

    # Draws entites to screen
    def renderEntities(self, win):
        for i in range(len(self.renderedStructureList)):
            self.renderedStructureList[i].render(win)

        for i in range(len(self.renderedMobList)):
            self.renderedMobList[i].render(win)

        for i in range(len(self.renderedItemList)):
            self.renderedItemList[i].render(win)

    # runs the primary function of every structure
    def runStructureFunctions(self, tickCount, playerObj, win):
        for i in range(len(self.structureList)):
            if type(self.structureList[i]) == Structure.BerryBush:
                self.structureList[i].growBerry(tickCount)

            if type(self.structureList[i]) == Structure.Cave:
                self.structureList[i].spawnWolf(playerObj,self.mobList, self.renderedMobList, win, tickCount)

        for i in range(len(self.renderedDestructableStructureList)):
            self.renderedDestructableStructureList[i].die(self.itemList, self.structureList)

    # runs mob functions
    def runMobFunctions(self, playerObj):
        for i in range(len(self.renderedMobList)):
            self.renderedMobList[i].die(self.mobList, self.itemList)
            self.renderedMobList[i].changeDir()
            self.renderedMobList[i].move()
            if isinstance(self.renderedMobList[i], HostileEntity.HostileEntity):
                self.renderedMobList[i].target(playerObj)

    # runs item functions
    def runItemFunctions(self, playerObj, inventory, win):
        for i in range(len(self.renderedItemList)):
            self.renderedItemList[i].pickup(playerObj, inventory, self.itemList)

    # everything moves relative to the player
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

    # player-entity interactions
    def playerInteract(self, playerObj, keys):
        if keys == "f":
            for i in range(len(self.renderedStructureList)):
                if int(math.sqrt((self.renderedStructureList[i].xCor-playerObj.xCor)**2+(self.renderedStructureList[i].yCor-playerObj.yCor)**2)) < 30 and type(self.renderedStructureList[i]) == Structure.BerryBush:
                    self.renderedStructureList[i].dropBerry(self.itemList)

        elif keys == "m1":
            for i in range(len(self.renderedMobList)):
                if int(math.sqrt((self.renderedMobList[i].xCor-playerObj.xCor)**2+(self.renderedMobList[i].yCor-playerObj.yCor)**2)) < 30:
                    self.renderedMobList[i].health -= 1

            for i in range(len(self.renderedStructureList)):
                if int(math.sqrt((self.renderedStructureList[i].xCor-playerObj.xCor)**2+(self.renderedStructureList[i].yCor-playerObj.yCor)**2)) < 30 and isinstance(self.renderedStructureList[i], Structure.DestructableStructure):
                    self.renderedStructureList[i].health -= 1
