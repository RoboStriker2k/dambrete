import pygame
import sys
from pygame.locals import *
from time import sleep

# speletaju krasas
#       R     G   B
Balts = (255, 255, 255)
Melns = (0,  0,  0)
fonakrasa =(37,216,85)
fons2krasa=(88,206,202)
# logu izmers
width = 800
height = 600

# speles iestatijumi
SpelesLaukumaIzmers = 8
kvadrataizmers = height/SpelesLaukumaIzmers

# Virzienu definicija
KA = "KA"  # kreisais augšejais
LA = "LA"  # labais augšējais
KZ = "KZ"  # Kreisais apakšejais/zemais
LZ = "LZ"  # Labais apakšējais/zemais

# PYGame iestatijumi
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Dambrete')
clock = pygame.time.Clock()
laukums = pygame.Surface((height, height))  # W H
kvadra = pygame.Surface((kvadrataizmers, kvadrataizmers))  # W H
kvadra.fill('white')
panelis2 = pygame.Surface((width-height, height))
font1 = pygame.font.Font(None, 50)
teksts = font1.render('Dambrete', False, 'black')

# importe attelus un parveido to izmeru
SP1att=pygame.image.load('atteli/speletajs1.png')
SP2att=pygame.image.load('atteli/speletajs2.png')
SP1datt=pygame.image.load('atteli/speletajs1dama.png')
SP2datt=pygame.image.load('atteli/speletajs2dama.png')
SP1att=pygame.transform.scale(SP1att,(kvadrataizmers,kvadrataizmers))
SP2att=pygame.transform.scale(SP2att,(kvadrataizmers,kvadrataizmers))
SP1datt=pygame.transform.scale(SP1datt,(kvadrataizmers,kvadrataizmers))
SP2datt=pygame.transform.scale(SP2datt,(kvadrataizmers,kvadrataizmers))
def main():
    Running = True  # Mainigais ar kuru vares partraukt programams darbibu patraucot while loop
    
    spele = Spele()
    laukumavertibas1 = spele.galds1.atgriezt_laukumu()
    lauc=spele.galds1.matrica
    print("Arpus glada check=",spele.galds1.ArPusGalda(0,2))
    print("Atlautie gajieni=",spele.galds1.atlautieGajieni(0,2))
    print("vispariga kustiba=",spele.galds1.vienkarsakustiba(0,2))    
    print("matrica 1 1=",spele.galds1.lokacija(0,2).aiznemts)    
    while Running == True:
        grafika()
        krasojums()
        grafKaul(lauc)
        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Running = False
                sys.exit()

# iekrāso kvadrātu laukumus


def krasojums():
    for x in range(SpelesLaukumaIzmers):
        for y in range(SpelesLaukumaIzmers):

            if (x % 2 != 0) and (y % 2 == 0):
                screen.blit(kvadra, (kvadrataizmers*x, kvadrataizmers*y))
            elif (x % 2 == 0) and (y % 2 != 0):
                screen.blit(kvadra, (kvadrataizmers*x, kvadrataizmers*y))
# Nodrosina parejo grafikas laukumu


def grafika():
    screen.blit(laukums, (0, 0))
    screen.blit(panelis2, (600, 0))
    laukums.fill(fonakrasa)
    panelis2.fill(fons2krasa)
    screen.blit(teksts, (600, 10))
# attelo kauliņus uz laukuma    
def grafKaul(matrica):
    for x in range(SpelesLaukumaIzmers):
        for y in range(SpelesLaukumaIzmers):
         if matrica[x][y].aiznemts!=None:
            if matrica[x][y].aiznemts.krasa==(255, 255, 255):
                screen.blit(SP1att, (kvadrataizmers*x, kvadrataizmers*y))
            elif matrica[x][y].aiznemts.krasa==(0,  0,  0):
                screen.blit(SP2att, (kvadrataizmers*x, kvadrataizmers*y))  
            else:
      
   
                pass
  

class Spele:
    """
    Speles sakums

    """

    def __init__(self):
        self.galds1 = Galds()


class Galds:
    def __init__(self):
        self.matrica = self.jaunaSpele()

    def jaunaSpele(self):
        # izveido jaunu laukumu
        matrica = [
            [None]*SpelesLaukumaIzmers for i in range(SpelesLaukumaIzmers)]
        # azipilda to ar lauciņiem
        for x in range(SpelesLaukumaIzmers):
            for y in range(SpelesLaukumaIzmers):
                if ((x % 2 > 0) and (y % 2 == 0)) or ((x % 2 == 0) and (y % 2 > 0)):
                    matrica[x][y] = laucins(Balts)
                elif ((x % 2 > 0) and (y % 2 > 0)) or ((x % 2 == 0) and (y % 2 == 0)):
                      matrica[x][y] = laucins(Melns)
               
        # aizpilda to ar kauliņiem
        for x in range(SpelesLaukumaIzmers):
            for y in range(3):
                if matrica[x][y].krasa == Melns:
                    matrica[x][y].aiznemts = kaulins(Melns)
                    #print(x,y,"melns") #printe kaulinu izvietojumu speles sakuma
            for y in range(SpelesLaukumaIzmers-3, SpelesLaukumaIzmers):
                if matrica[x][y].krasa == Melns:
                    matrica[x][y].aiznemts = kaulins(Balts)
                    #print(x,y,"balts") #printe kaulinu izvietojumu speles sakuma

        return matrica

    def atgriezt_laukumu(self):
        laukumavertibas = [[None]*SpelesLaukumaIzmers]*SpelesLaukumaIzmers
        for x in range(SpelesLaukumaIzmers):
            for y in range(SpelesLaukumaIzmers):
                if self.matrica[x][y].krasa == Balts:
                    laukumavertibas[x][y] = "Balts"
                    #   print(x,y, "Balts")
                elif self.matrica[x][y].krasa == Melns:
                    laukumavertibas[x][y] = "Melns"
                   # print(x,y, "Melns")
                else:
                    laukumavertibas[x][y] = "Tukšs"
                    # print(x,y, "Tukšs")
        return laukumavertibas

    def lokacija(self, x, y):
        x = int(x)
        y = int(y)
        return self.matrica[x][y]

    def relativitate(self, virziens, x, y):
        match virziens:
            case "KZ":
                return (x-1, y+1)
            case "LZ":
                return (x+1, y+1)
            case "KA":
                return (x-1, y-1)
            case "LA":
                return (x+1, y-1)
            case _:
                return 0
    #atgriez apkartejos laucinuss
    def apkartejie(self, x, y):
        return [self.relativitate(KA, x, y), self.relativitate(LA, x, y), self.relativitate(KZ, x, y), self.relativitate(LZ, x, y)]
    #atgriez visus gajienus kaulinam
    def vienkarsakustiba(self,x,y):

        if self.matrica[x][y].aiznemts!=None:
            if self.matrica[x][y].aiznemts.dama==False and self.matrica[x][y].aiznemts.krasa==(255, 255, 255):
                gajiens=[self.relativitate(KA,x,y),self.relativitate(LA,x,y)]
            elif self.matrica[x][y].aiznemts.dama==False and self.matrica[x][y].aiznemts.krasa==(0, 0, 0):    
                gajiens=[self.relativitate(KZ,x,y),self.relativitate(LZ,x,y)]
            else:
                gajiens=[self.relativitate(KZ,x,y),self.relativitate(LZ,x,y),self.relativitate(KA,x,y),self.relativitate(LA,x,y)]  
        else:
            gajiens=[]
            
        return gajiens
    # parbauda vai kordinate arpus galda 
    def ArPusGalda (self,x,y):
        if x<0 or y<0 or x>SpelesLaukumaIzmers or y>SpelesLaukumaIzmers:
            return True
        else:
            return False
    # Aizvieto kaulinu at tukšu vietu.
    def NonemtKaulinu(self,x,y):
        self.matrica[x][y].aiznemts=None
    # Veic Kustību
    def kustiba(self,x0,y0,x1,y1):
        m=self.matrica
        m[x1][y1]=m[x0][y0].copy()
        m[x0][y0].aiznemts=None
        self.kronet(x1,y1)
    #atgriez atlautos gajienus    
    def atlautieGajieni(self,x,y,lekt=False) :
        #vk- vienkarsa kustiba | AG- atlautie gajieni|  ga- gajiens | m matrica | mat - matrica ar kordinatem no gajiena
        m=self.matrica
        VK=self.vienkarsakustiba(x,y)
        AG=[]
        if not lekt:
            for ga in VK:
                mat=m[ga[0]][ga[1]]
                if not self.ArPusGalda(ga[0],ga[1]):
                    if mat.aiznemts==None:
                        AG.append(ga)
                    elif mat.aiznemts.krasa != m[x][y].aiznemts.krasa and not self.ArPusGalda(ga[0]+(ga[0]-x),ga[1]+(ga[1]-y)) and m[ga[0]+(ga[0]-x)][ga[1]+(ga[1]-y)].aiznemts==None:
                        AG.append((ga[0]+(ga[0]-x),ga[1]+(ga[1]-y)))
        else:
            for gajieni in VK:
                pass    
            
        return AG    
    
    def kronet(self,x,y):
       if self.matrica[x][y].aiznemts!=None: 
        if (self.matrica[x][y].aiznemts.krasa==(255,255,255) and y==0) or(self.matrica[x][y].azinemts.krasa==(0,0,0) and y==SpelesLaukumaIzmers):
            self.matrica[x][y].aiznemts.dama()
            
                
######################################## Kaulina definicija ############################################
class kaulins:
    def __init__(self, krasa, dama=False):
        self.krasa = krasa
        self.dama = dama
        self.vertiba = 1 

    def dama(self):
        self.dama = True
        self.vertiba = 2
######################################### Laucina definicija  ##########################################


class laucins:
    def __init__(self, krasa, aiznemts=None):
        self.krasa = krasa
        self.aiznemts = aiznemts


######################################## INICIALIZE MAIN FUNKCIJU #################################################
if __name__ == "__main__":
    main()
    pass
