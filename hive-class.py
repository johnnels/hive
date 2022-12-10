import pygame
from sys import exit

import random


#basic setup
screen_width = 850
screen_height = 650
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('hive')
clock = pygame.time.Clock()

#fonts
pix_font = pygame.font.Font('graphics/Pixeltype.ttf', 32)

#image holders
bg_img = pygame.Surface((screen_width,screen_height))
bg_img.fill('Black')

playerStorage = []
print (len(playerStorage))
class Player:
    def __init__(self, x, y, slot):
        self.img = pygame.Surface((48, 48))
        self.img.fill('Red')
        self.x = x
        self.y = y
        self.vel = .6
        self.xvel = 0
        self.yvel = 0
        self.maxvel = 4
        self.slot = slot
        self.slot_surf = pix_font.render(str(self.slot), False, 'white')



    def update(self):
        # Reduce velocity to zero if near zero
        if abs(self.xvel) < 0.2:
            self.xvel = 0
        if abs(self.yvel) < 0.2:
            self.yvel = 0

        # Move object
        self.x += self.xvel
        self.y += self.yvel

        #slow object
        self.xvel = self.xvel * .85
        self.yvel = self.yvel * .85

        #Limit speed
        if (abs(self.xvel) + abs(self.yvel)) > self.maxvel:
            self.xvel = self.xvel * (self.maxvel / (abs(self.xvel) + abs(self.yvel)))
            self.yvel = self.yvel * (self.maxvel / (abs(self.yvel) + abs(self.xvel)))

        #Draw object
        screen.blit(self.img,(self.x,self.y))
        screen.blit(self.slot_surf,(self.x+4,self.y+4))


def keyCheck(selected):
    global selectedPlr
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        selectedPlr = playerStorage[0]
        print(selectedPlr)
    if keys[pygame.K_2]:
        if (len(playerStorage) > 1): selectedPlr = playerStorage[1]
        print(selectedPlr)
    if keys[pygame.K_d]: # right
        selected.xvel += selected.vel
    if keys[pygame.K_a]: # left
        selected.xvel -= selected.vel
    if keys[pygame.K_w]: # up
        selected.yvel -= selected.vel
    if keys[pygame.K_s]: # down
        selected.yvel += selected.vel



for i in range(6):
    playerStorage.append(Player(random.randrange(24,screen_width-24),random.randrange(24,screen_height-24),len(playerStorage)+1))

selectedPlr = playerStorage[0]
#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('quiting')
            pygame.quit()
            exit()

    keyCheck(selectedPlr)
    screen.blit(bg_img,(0,0))
    for x in range(len(playerStorage)):
        playerStorage[x].update()

    pygame.display.update()
    clock.tick(60)
