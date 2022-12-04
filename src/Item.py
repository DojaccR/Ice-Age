class Item:
    itemID = 0
    itemName = ""
    itemTexture = ""
    isPickedUp = False
    xCor = 0
    yCor = 0
    

    def __init__(self, itemID, itemName, xCor, yCor):
        self.itemID = itemID
        self.itemName = itemName
        self.xCor = xCor
        self.yCor = yCor

class Clothing(Item):
    itemStackMax = 1


class Tool(Item):
    itemStackMax = 1


class Consumable(Item):
    def __init__(self):
        super().__init__()


    itemStackMax = 15


class Berry(Consumable):
    def __init__(self):
        super().__init__()
        self.itemTexture = "assets/Berry.png"