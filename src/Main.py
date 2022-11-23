#from GUI import *
#from Entity import *
from Player import *
import pygame

#window loading
pygame.init()

win = pygame.display.set_mode((1280,720))

pygame.display.set_caption("Ice Age")
pygame.display.set_icon(pygame.image.load('assets/Logo.png'))


#player loading
playerObj = Player(1, 100, 100, 200, 200, 4)
playerImage = pygame.image.load(playerObj.entityImageFile)

def player():
    win.blit(playerImage, (playerObj.xCor, playerObj.yCor))

def health():
    win.blit(pygame.image.load(playerObj.healthImageFile[4-playerObj.health]), (playerObj.xCor, playerObj.yCor+60))

#game loop
gameTick = 0
run = True

while playerObj.health > 0:
    pygame.time.delay(10)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and playerObj.xCor > 0:
        playerObj.xCor-= playerObj.vel

    if keys[pygame.K_RIGHT] and playerObj.xCor < 1280 - playerObj.hitboxWidth:
        playerObj.xCor+= playerObj.vel

    if keys[pygame.K_UP] and playerObj.yCor > 0:
        playerObj.yCor-= playerObj.vel

    if keys[pygame.K_DOWN] and playerObj.yCor < 720 - playerObj.hitboxHeight:
        playerObj.yCor+= playerObj.vel

    
    
    win.fill((0,255,0))

    #pygame.draw.rect(win, (0,0,255), (x, y, width, height))
    player()
    health()
    gameTick+=1
    pygame.display.update()

pygame.quit()
#player = Player
#player.__init__(player, 1, [20, 20], [0, 0], 10)




