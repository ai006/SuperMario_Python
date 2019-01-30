import pygame


from pygame.locals import*
from Sprite import Sprite

class Tube(Sprite):
    def __init__(self,model,xx = 200, yy = 200):
        self.x = xx
        self.y = yy
        self.w = 64
        self.h = 499
        self.model = model 
        self.tube_image = pygame.image.load("tube.png")
        self.rect = self.tube_image.get_rect()
        
    def drawSelf(self,v):
        v.screen.blit(self.tube_image,(self.x,self.y +100))
    
    def update(self):
        pass
        
    def returnImage(self):
        return self.tube_image