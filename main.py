import pygame ,sys
from pygame.locals import *
from time import sleep

# speletaju krasas
#       R     G   B  
white =(255,255,255)
black =(0  ,  0,  0)
#logu izmers
width =800
height=600

def main():
    Running= True
    while Running==True:
        screen=pygame.display.set_mode((width,height))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                Running= False
            
        
        
        

    
class spele:
    """
    Speles sakums

    """
    pass    
    
    
    
class Galds:
    def __init__(self):
        pass


class kaulins:
    def __init__(self, krasa,dama=False):
        self.krasa=krasa
        self.dama=dama
        self.vertiba=1
        
    def dama(self):
        self.dama=True
        self.vertiba=2
        
if __name__=="__main__":
    main()
    pass        