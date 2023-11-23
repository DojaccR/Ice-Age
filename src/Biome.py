import random as r

class Biome:
    def __init__(self, center):
        self.center = center
        self.border = self.createBorder()
        self.biomeType = None

    def createBorder(self):
        border = []

        return border

    def setBiomeType(self, biomeType):
        self.biomeType = biomeType