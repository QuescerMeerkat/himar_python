import pygame
from bullet import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        global x,y, x, y
        super().__init__()
        self.image=pygame.Surface((20,80))
        self.image.fill("White")
       
        self.rect=self.image.get_rect(center =(x,y))
       
    def update(self, screen_height):
        global x,y, playerspeed
        keys=pygame.key.get_pressed()

       

        if keys[pygame.K_DOWN] and playerspeed<0:
            bullet1.create_bullet()
            playerspeed*=-1

        if y >=screen_height-55:
                y=screen_height-55
                playerspeed*=-1

        if y<55:
            y=55
            playerspeed*=-1
               
        if keys[pygame.K_UP] and playerspeed>0:
            bullet1.create_bullet()
            playerspeed*=-1
        y+=playerspeed
        self.rect.center=(x,y)

##utilizar balas con movimiento en x y en y. eg (4,5) 1,2 4,2

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        global x2,y2
        super().__init__()
        self.image=pygame.Surface((20,80))
        self.image.fill("White")
       
        self.rect=self.image.get_rect(center =(x2,y2))
       
    def update(self, screen_height):
        global x2,y2, playerspeed2
        keys=pygame.key.get_pressed()

       

        if keys[pygame.K_s] and playerspeed2<0:
            bullet2.create_bullet2()
            playerspeed2*=-1

        if y2 >=screen_height-55:
                y2=screen_height-55
                playerspeed2*=-1

        if y2<55:
            y2=55
            playerspeed2*=-1
               
        if keys[pygame.K_w] and playerspeed2>0:
            bullet2.create_bullet2()
            playerspeed2*=-1
        y2+=playerspeed2
       
       
        self.rect.center=(x2,y2)