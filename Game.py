import pygame
import time
import Sprite


from pygame.locals import*
from time import sleep
from Sprite import Sprite
from myVegeta import Vegeta
from myTube import Tube
from myGoomba import Goomba
from myFireball import Fireball

class Model():
    def __init__(self):
         self.dest_x = 0
         self.dest_y = 0
         self.frame_count = 0
         self.sprites = []
         self.vegeta = Vegeta(self)
         self.sprites.append(self.vegeta)
         self.tubes = Tube(self,250,300)
         self.sprites.append(self.tubes)
         self.tubes = Tube(self,600,300)
         self.sprites.append(self.tubes)
         self.goomba = Goomba(self)
         self.sprites.append(self.goomba)
         
    def addFireball(self):
        self.fireball = Fireball(self,self.vegeta.x,self.vegeta.y)
        self.sprites.append(self.fireball)
        
    def update(self):
        if self.rect.left < self.dest_x:
            self.rect.left += 1
        if self.rect.left > self.dest_x:
            self.rect.left -= 1
        if self.rect.top < self.dest_y:
            self.rect.top += 1
        if self.rect.top > self.dest_y:
            self.rect.top -= 1
        if self.frame_count > 3:
            self.frame_count = 0
            
        for i in self.sprites:
            i.update()
            if i.isGoomba():
                if i.fc > 5 and i.hit:
                    self.sprites.remove(i)
            if i.isFireball():
                if i.touched:
                    self.sprites.remove(i)
            
        

    def set_dest(self, pos):
        self.dest_x = pos[0]
        self.dest_y = pos[1]

class View():
    def __init__(self, model):
        screen_size = (800,600)
        self.screen = pygame.display.set_mode(screen_size, 32)
        self.model = model
        self.vegeta_image = [pygame.image.load("S0.png"),pygame.image.load("S2.png"),pygame.image.load("S3.png"),pygame.image.load("S4.png")]
        self.model.rect = self.vegeta_image[0].get_rect()

    def update(self):    
            self.screen.fill([0,200,100])
            #self.screen.blit(self.vegeta_image[self.model.frame_count], (self.model.vegeta.x,self.model.vegeta.y))
            for i in self.model.sprites:
                i.drawSelf(self)
            pygame.display.flip()
            
            

class Controller():
    def __init__(self, model):
        self.model = model
        self.keep_going = True

    def update(self):
        self.model.vegeta.prev_x = self.model.vegeta.x
        self.model.vegeta.prev_y = self.model.vegeta.y
        for event in pygame.event.get():
            if event.type == QUIT:
                self.keep_going = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.keep_going = False
            elif event.type == pygame.MOUSEBUTTONUP:
                self.model.set_dest(pygame.mouse.get_pos())
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.model.vegeta.x -= 5
            self.model.frame_count+= 1
        if keys[K_RIGHT]:
            self.model.vegeta.x += 5
            self.model.frame_count+= 1
            #Vegeta.hi(self)
            #Vegeta.hey(self)
        if keys[K_UP]:
           self.model.dest_y -= 1
        if keys[K_DOWN]:
            self.model.dest_y += 1
            self.model.vegeta.vert_velociy -= 18
        if keys[K_SPACE] and self.model.vegeta.onGround < 3:
            self.model.vegeta.jump()
        if keys[K_LCTRL]:
            self.model.addFireball()

print("Use the arrow keys to move. Press Esc to quit.")
pygame.init()
m = Model()
v = View(m)
c = Controller(m)
while c.keep_going:
	c.update()
	m.update()
	v.update()
	sleep(0.04)
print("Goodbye")