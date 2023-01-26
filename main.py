import pygame, random, time
from player import *
from bullet import *
from randomobjects import *

pygame.init()
clock=pygame.time.Clock()

screen_height=600
screen_width=800

screen= pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("shooting game")

playerspeed=random.choice([5,-5])
playerspeed2=random.choice([5,-5])
array=[]
array2=[]
x,y=screen_width/2+250, screen_height/2
x2,y2=screen_width/2-250, screen_height/2
pygame.mouse.set_visible(True)
counter=1
       

def update_draw_groups():
    global grouplist
    for group in grouplist:
        group.update()
        group.draw(screen)

def createrandom():
    global counter
    while counter<=2:
        randomobject.add(randomobjects(random.randrange(250,550),random.randrange(100,screen_height-100)))
       
        counter+=1
       
class rock(pygame.sprite.Sprite):
    def __init__(self,posx,posy):

        super().__init__()
        self.image=pygame.Surface((40,40))
        self.image.fill("Purple")

        self.rect=self.image.get_rect(center=(posx,posy))
    def update(self):
        pass

    
counter2=0
def createrock():
    global counter2
    while counter2<=2:
        rockgroup.add(rock(random.randrange(250,550),random.randrange(100,screen_height-100)))
        
        counter2+=1

   
   
player2= Player2()
player_group2=pygame.sprite.Group()
player_group2.add(player2)

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

extremebullets=[pygame.sprite.Group() for i in range(4)]

bulletgroup = pygame.sprite.Group()
bulletgroup2 = pygame.sprite.Group()

randomobject=pygame.sprite.Group()
rockgroup=pygame.sprite.Group()
grouplist=[extremebullet for i in range(len(extremebullets))]

run=True

while run:
   
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

   
   
    screen.fill("Light Blue")

    bulletgroup2.draw(screen)
    bulletgroup.draw(screen)

    player_group2.draw(screen)
    player_group.draw(screen)
   
    collisions=pygame.sprite.groupcollide(bulletgroup, bulletgroup2, True, True)
   
    bulletgroup.update(array, player2, randomobject)
    bulletgroup2.update(array2, screen_width, randomobject, player)

    player_group.update(screen_height)
    player_group2.update(screen_height)

    createrandom()

    randomobject.draw(screen)

    createrock()
    rockgroup.update()
    rockgroup.draw(screen)
    

    update_draw_groups()

    
   

    pygame.display.update()
pygame.quit()