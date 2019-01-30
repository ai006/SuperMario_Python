import pygame


from pygame.locals import*
from Sprite import Sprite

class Vegeta(Sprite):
    def __init__(self, model):
        self.x = 50
        self.y = 50
        self.w = 48
        self.h = 48
        self.prev_x = 0
        self.prev_y = 0
        self.model = model
        self.vegeta_image = [pygame.image.load("S0.png"),pygame.image.load("S2.png"),pygame.image.load("S3.png"),pygame.image.load("S4.png")]
        self.rect = self.vegeta_image[0].get_rect()
        self.vert_velociy = -12.0
        self.onGround = 0
        
    def hi(self):
        print("yooooo")
    
    def drawSelf(self,v):
        v.screen.blit(self.vegeta_image[self.model.frame_count], (self.x,self.y))
    
    def update(self):
        self.vert_velociy += 1.9
        self.y += self.vert_velociy
        
        if(self.y > 400):
            self.vert_velociy = 0
            self.y = 400
            self.onGround = 0
        self.onGround+= 1
        for s in self.model.sprites:
            if((self.didItCollide(s)) and not( s.isVegeta())):
                if(self.x + self.w >= s.x and self.prev_x + self.w < s.x ):
                    self.x = s.x - self.w -2
                if(self.x <= s.x + s.w and self.prev_x > s.x + s.w):
                    self.x = s.x + s.w + 1
                if(self.y >= s.y and self.prev_y < s.y): 
                     self.y = s.y - 5
                     self.onGround = 0
                     self.vert_velocity = 0
                     
                else:
                    print("How did I get in here?")
                
            
    def jump(self):
        self.vert_velociy -=17
        
    def isVegeta(self):
        return True
        
        
    def returnImage(self):
        return self.vegeta_image[self.model.frame_count]