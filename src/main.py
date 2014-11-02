import pygame, sys, other
from pygame.locals import *


Inv = other.Inventory
Item = other.Item
Items = other.Item.Items

deslize = "Deslize.jpg"
cursor = "cursor.png"

#pygame.init()

#screen = pygame.display.set_mode((750,550),0,32)
#pygame.mouse.set_visible(False)

#background = pygame.image.load(deslize).convert()
#mouse_c = pygame.image.load(cursor).convert_alpha()

#movex,movey = 0,0
#x,y = 0,0

#clock = pygame.time.Clock()
#speed = 5

ShortSword = Item('Sword','Short Sword')
IronShield = Item('Shield','Iron Shield')
HealthPotion = Item('Consumable','Health Potion',True,10)

playerInventory = Inv('playerInventory',15)
monsterInventory = Inv('mInventory',5)

playerInventory.addItem(HealthPotion,5)
playerInventory.addItem(ShortSword,2)
playerInventory.addItem(IronShield)
playerInventory.addItem(HealthPotion,5)

playerInventory.addItem(HealthPotion,3)
playerInventory.addItem(HealthPotion,3)

monsterInventory.addItem(ShortSword)

playerInventory.printInventory()
print ('--')
monsterInventory.printInventory()





input('Continue...')


#while True:
#    for event in pygame.event.get():
#        x,y = pygame.mouse.get_pos()  
#        if event.type == QUIT:
#            pygame.quit()
#            sys.exit()
#          
#        if event.type == KEYDOWN:
#            if event.key == K_LEFT:
#                movex = -0.5
#            elif event.key == K_RIGHT:
#                movex = +0.5
#            elif event.key == K_UP:
#                movey = -0.5
#            elif event.key == K_DOWN:
#                movey = +0.5
#            elif event.key == K_ESCAPE:
#                pygame.quit()
#                sys.exit()
#        if event.type == KEYUP:
#            if event.key == K_LEFT:
#                movex = 0
#            elif event.key == K_RIGHT:
#                movex = 0
#            elif event.key == K_UP:
#                movey = 0
#            elif event.key == K_DOWN:
#                movey = 0
                
#    x+= movex
#    y+= movey          
    
#    mill = clock.tick()
#    seconds = mill/1000.
#    DM = seconds*speed              
            
#    screen.fill((0,0,0))
#    screen.blit(mouse_c,(x,y))     
    
#    pygame.display.update()