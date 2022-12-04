class InventorySlot:
    content = None
    slotID = None

    def __init__(self, slotID):
        self.slotID = slotID

    def swopItem(self, item1, item2, slot):
        self.content = item1
        slot.content = item2
