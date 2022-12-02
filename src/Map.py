import os


class Map:
    mapID = 0
    mapFile = ""
    mapTiles = []

    def __init__(self, mapID):
        if str(mapID) == "create":
            map = open("map1.txt", "w")
        else:
            map = open("map1.txt")
            mapStr = map.read()
            self.mapTiles = [*mapStr]
    
