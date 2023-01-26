import pygame
        
class bullet1(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
       
        super().__init__()
        self.image=pygame.Surface((40,10))
        self.image.fill("Red")
       
        self.rect= self.image.get_rect(center=(pos_x, pos_y))

    def create_bullet(bulletgroup, array, x, y):
       
        if array==[]:
            return bulletgroup.add(bullet1(x-15,y))
       
       
        if abs(array[-1]-y)>80:
            array=[]
            return bulletgroup.add(bullet1(x-15,y))

    def getting_less_hearts():
        pass

    def update(self, array, player2, randomobject):
        if self.rect.y not in array:
            array.append(self.rect.y)
        self.rect.x-=3
   
        if self.rect.x<-20:
            array.remove(self.rect.y)
            self.kill()

        if self.rect.colliderect(player2):
            bullet1.getting_less_hearts()

        for ob in randomobject:
            if self.rect.colliderect(ob):
                posx=self.rect.x
                posy=self.rect.y
                self.kill()
                ob.kill()
                randomobject.update(posx,posy,2)

class bullet2(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
       
        super().__init__()
        self.image=pygame.Surface((40,10))
        self.image.fill("Red")
       
        self.rect= self.image.get_rect(center=(pos_x, pos_y))

    def create_bullet2(bulletgroup2, array2, x2, y2):
        if array2==[]:
            return bulletgroup2.add(bullet2(x2+15,y2))
       
       
        if abs(array2[-1]-y2)>80:
            array2=[]
            return bulletgroup2.add(bullet2(x2+15,y2))

    def getting_less_hearts():
        pass

    def update(self, array2, screen_width, randomobject, player):
        if self.rect.y not in array2:
            array2.append(self.rect.y)
        self.rect.x+=3
       
        if self.rect.x>screen_width-100:
            array2.remove(self.rect.y)
            self.kill()

        if self.rect.colliderect(player):
           bullet2.getting_less_hearts()

        for ob in randomobject:
            if self.rect.colliderect(ob):
                posx=self.rect.x
                posy=self.rect.y
                self.kill()
                ob.kill()
                randomobject.update(posx,posy,1)

class extremebullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y,group):
        super().__init__()
        self.image=pygame.Surface((40,10))
        self.image.fill("Red")
        self.rect= self.image.get_rect(center=(pos_x, pos_y))
        self.group=group

    def update(self, extremebullets, randomobject):
        if self.group==extremebullet[0]:
            self.rect.x+=3
            self.rect.y+=1
            for ob in randomobject:
                if self.rect.colliderect(ob):
                    posx=self.rect.x
                    posy=self.rect.y
                    self.kill()
                    ob.kill()
                    randomobject.update(posx,posy,1)

                    
        if self.group==extremebullet[1]:
            self.rect.x+=3
            self.rect.y-=1
            for ob in randomobject:
                if self.rect.colliderect(ob):
                    posx=self.rect.x
                    posy=self.rect.y
                    self.kill()
                    ob.kill()
                    randomobject.update(posx,posy,1)
                    
        if self.group==extremebullet[2]:
            self.rect.x-=3
            self.rect.y-=1
            for ob in randomobject:
                if self.rect.colliderect(ob):
                    posx=self.rect.x
                    posy=self.rect.y
                    self.kill()
                    ob.kill()
                    randomobject.update(posx,posy,2)
                    
        if self.group==extremebullet[3]:
            self.rect.x-=3
            self.rect.y+=1
            for ob in randomobject:
                if self.rect.colliderect(ob):
                    posx=self.rect.x
                    posy=self.rect.y
                    self.kill()
                    ob.kill()
                    randomobject.update(posx,posy,2)
               