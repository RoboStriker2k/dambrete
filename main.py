import pygame ,sys
from pygame.locals import *
from time import sleep

# speletaju krasas
#       R     G   B  
Balts =(255,255,255)
Melns =(0  ,  0,  0)
#logu izmers
width =800
height=600

# speles iestatijumi
SpelesLaukumaIzmers=8
kvadrataizmers=height/SpelesLaukumaIzmers

# Virzienu definicija
KA="KA" # kreisais augšejais
LA="LA" # labais augšējais
KZ="KZ" # Kreisais apakšejais/zemais
LZ="LZ" # Labais apakšējais/zemais

# PYGame iestatijumi
pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Dambrete')
clock=pygame.time.Clock()
laukums=pygame.Surface((height,height)) # W H
kvadra=pygame.Surface((kvadrataizmers,kvadrataizmers)) # W H
kvadra.fill('white')
panelis2=pygame.Surface((width-height,height))
font1=pygame.font.Font(None,50)   
teksts=font1.render('Dambrete',False,'black')


def main():
    Running= True #Mainigais ar kuru vares partraukt programams darbibu patraucot while loop

    spele=Spele()

    while Running==True:
        grafika()
        krasojums()
        pygame.display.update()    
        clock.tick(60)

        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                Running= False
                sys.exit()
                
# iekrāso kvadrātu laukumus                 
def krasojums():
    for x in range(SpelesLaukumaIzmers):
            for y in range(SpelesLaukumaIzmers):    
                    
                if (x%2 !=0) and (y%2==0):
                    screen.blit(kvadra,(kvadrataizmers*x,kvadrataizmers*y))
                elif (x%2 ==0) and (y%2!=0):
                    screen.blit(kvadra,(kvadrataizmers*x,kvadrataizmers*y))  
# Nodrosina parejo grafikas laukumu      
def grafika():
    screen.blit(laukums,(0,0))
    screen.blit(panelis2,(600,0))
    laukums.fill('chocolate')
    panelis2.fill('Red')
    screen.blit(teksts,(600,10) )
        


    
class Spele:
    """
    Speles sakums

    """
    def __init__(self):
       self.galds1=Galds()
 
       
        
    
    
    
class Galds:
    def __init__(self):
        self.matrica=self.jaunaSpele()
    def jaunaSpele(self):
        #izveido jaunu laukumu
        matrica=[[None]*SpelesLaukumaIzmers for i in range(SpelesLaukumaIzmers)]
        #azipilda to ar kauliņiem
        for x in range(SpelesLaukumaIzmers):
            for y in range(SpelesLaukumaIzmers):    
                if (x%2 !=0) and (y%2==0):
                    matrica[y][x]=laucins(Balts,kaulins(Balts))
                elif (x%2!=0) and (y%2 !=0):
                    matrica[y][x]=laucins(Melns,kaulins(Melns))
                elif (x%2 ==0) and (y%2!=0):
                    matrica[y][x]=laucins(Balts,kaulins(Balts))
                elif (x%2==0) and (y%2 ==0):
                    matrica[y][x]=laucins(Melns,kaulins(Melns))             
        return matrica
    
                
    def atgriezt_laukumu(self,galds):
        laukumavertibas=[[None]*SpelesLaukumaIzmers]*SpelesLaukumaIzmers            
        for x in range(SpelesLaukumaIzmers):
            for y in range(SpelesLaukumaIzmers):
                if galds[x][y].krasa==Balts:
                    laukumavertibas  [x][y]="Balts"
                elif galds[x][y].krasa==Melns:
                    laukumavertibas  [x][y]="Melns"   
                else:
                    laukumavertibas  [x][y]="Tukšs"      
        return laukumavertibas      
 

                  
    def lokacija(self,x,y):
        x=int(x)
        y=int(y)
        return self.matrica[x][y]
    
    def relativitate(self,virziens,x,y):
        match virziens:
            case "KZ":
                return(x-1,y+1)
            case "LZ":
                return(x+1,y+1)
            case "KA":
                return(x-1,y-1)
            case "LA":
                return(x+1,y-1)
            case _:
                return 0                                                  
    def apkartejie(self,x,y):
          return [self.relativitate(KA,x,y),self.relativitate(LA,x,y),self.relativitate(KZ,x,y),self.relativitate(LZ,x,y)]
######################################## Kaulina definicija ############################################
class kaulins:
    def __init__(self, krasa,dama=False):
        self.krasa=krasa
        self.dama=dama
        self.vertiba=1
        
    def dama(self):
        self.dama=True
        self.vertiba=2
######################################### Laucina definicija  ##########################################
class laucins:
    def __init__(self,krasa,aiznemts=None):
        self.krasa=krasa
        self.aiznemts=aiznemts
               
        
######################################## INICIALIZE MAIN FUNKCIJU #################################################         
if __name__=="__main__":
    main()
    pass        