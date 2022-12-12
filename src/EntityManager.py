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

    def renderEntities(self, win):
        for i in range(len(self.renderedStructureList)):
            self.renderedStructureList[i].render(win)

        for i in range(len(self.renderedMobList)):
            self.renderedMobList[i].render(win)

        for i in range(len(self.renderedItemList)):
            self.renderedItemList[i].render(win)

    def runStructureFunctions(self):
        pass
