import pygame, random
from bullet import *

class randomobjects(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        global posx, posy
        super().__init__()
        self.image=pygame.Surface((40,40))
        self.image.fill("Grey")

        self.rect=self.image.get_rect(center=(pos_x,pos_y))

    def update(self, extremebullets, randomobject, posx, posy, dec, screen_height):
        if dec==1:
            extremebullet[0].add(extremebullet(posx,posy,extremebullet[0]))
            extremebullet[1].add(extremebullet(posx,posy,extremebullet[1]))
        if dec==2:
            extremebullet[2].add(extremebullet(posx,posy,extremebullet[2]))
            extremebullet[3].add(extremebullet(posx,posy,extremebullet[3]))
        randomobject.add(randomobjects(random.randrange(250,550),random.randrange(100,screen_height-100)))