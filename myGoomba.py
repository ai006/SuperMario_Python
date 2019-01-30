import pygame


from pygame.locals import*
from Sprite import Sprite

class Goomba(Sprite):
    def __init__(self, model):
        self.x = 320
        self.y = 400
        self.w = 99
        self.h = 118
        self.model = model
        self.goomba_image = pygame.image.load("gumba.png")
        self.fireGoomba_image = pygame.image.load("gumba_fire.png")
        self.rect = self.goomba_image.get_rect()
        self.vert_velociy = -12.0
        self.move = True
        self.hit = False
        self.fc = 0
        
    
    def drawSelf(self,v):
        if not self.hit:
            v.screen.blit(self.goomba_image, (self.x,self.y))
        else:
            v.screen.blit(self.fireGoomba_image,(self.x,self.y))
    
    def update(self):
        if self.move:
            self.x -= 5
        else:
            self.x += 5
        if self.hit:
            self.fc += 1
           
        for s in self.model.sprites:
            if((self.didItCollide(s)) and not( s.isGoomba())):
                self.move = not(self.move)
                print("we have a collision")
            if((self.didItCollide(s)) and s.isFireball()):
                self.hit = True
                self.model.fireball.touched = True
            
    def jump(self):
        self.vert_velociy -=17
        
    def isGoomba(self):
        return True
        
        
    def returnImage(self):
        return self.vegeta_image[self.model.frame_count]