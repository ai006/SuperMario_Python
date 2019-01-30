import pygame


from pygame.locals import*
from Sprite import Sprite

class Fireball(Sprite):
    def __init__(self, model, xx = 50 , yy = 50):
        self.x = xx
        self.y = yy
        self.w = 47
        self.h = 47
        self.vert_velocity = 3.0; 
        self.hor_velocity = 3.0;
        self.model = model
        self.fireball_image = pygame.image.load("fireball.png")
        self.rect = self.fireball_image.get_rect()
        self.i  = 0
        self.touched = False
        
    def drawSelf(self,v):
        v.screen.blit(self.fireball_image, (self.x,self.y))
    
    def update(self):
        self.x += self.hor_velocity;
       
        if self.i == 0:
            self.y-= self.vert_velocity
            if(self.y < 400):
                self.i = 1
        else:
            self.y+= self.vert_velocity
            if(self.y > 450):
                self.i = 0
                
    def isFireball(self):
        return True