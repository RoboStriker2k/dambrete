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

# speles iestatijumi
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Dambrete')
clock=pygame.time.Clock()
laukums=pygame.Surface((600,600)) # W H
panelis2=pygame.Surface((200,600))
def main():
    Running= True
    while Running==True:
        screen.blit(laukums,(0,0))
        screen.blit(panelis2,(600,0))
        laukums.fill('chocolate')
        panelis2.fill('Red')
        
        pygame.display.update()    
        clock.tick(60)
        
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