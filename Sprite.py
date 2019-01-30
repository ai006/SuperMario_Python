


class Sprite():
    def __init__(self):
        x = 50
        y = 50
        
    def hi(self):
        print("hey")
    
    def drawSelf(self,views):
        pass
        
    def isVegeta(self):
        return False
        
    def isGoomba(self):
        return False
        
    def isFireball(self):
        return False
        
    def update(self):
        pass

    def didItCollides(self,s):
        if self.x + self.w < s.x:
            return False
        if self.x > s.x + s.w:
            return False
        if self.y > s.y:
            return False
        if self.y > s.y + s.h:
            return False
        return True 
        
    def didItCollide(self,s):
        if s.x + s.w < self.x:
            return False
        if s.x > self.x + self.w:
            return False
        if s.y > self.y:
            return False
        if s.y > self.y + self.h:
            return False
        return True