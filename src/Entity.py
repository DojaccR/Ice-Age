class Entity:
    entityID = 0
    hitbox = [0,0]
    coords = [0,0]
    xvel = 0
    yvel = 0
    health = 0
    dropTable = [0]

    def __init__(self, entityID, hitbox, coords, health):
        self.entityID = entityID
        self.hitbox = hitbox
        self.coords = coords
        self.health = health

    def move():
        pass

    def health(healthchange):
        health += healthchange

    def die():
        pass
