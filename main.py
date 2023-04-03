import pygame
import sys
from pygame.locals import *
from time import sleep

# speletaju krasas
#       R     G   B
Balts = (255, 255, 255)
Melns = (0,  0,  0)
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

# importe attelus
SP1att=pygame.image.load('atteli/speletajs1.png')
SP2att=pygame.image.load('atteli/speletajs2.png')
SP1datt=pygame.image.load('atteli/speletajs1dama.png')
SP2datt=pygame.image.load('atteli/speletajs2dama.png')

def main():
    Running = True  # Mainigais ar kuru vares partraukt programams darbibu patraucot while loop
    
    spele = Spele()
    laukumavertibas1 = spele.galds1.atgriezt_laukumu()
    lauc=spele.galds1.matrica

    """
    print(lauc[1][1].krasa,lauc[1][2].krasa)
    print(lauc[2][1].krasa,lauc[2][2].krasa)
    print(lauc[1][1].aiznemts.krasa,lauc[1][2].aiznemts)
    print(lauc[2][1].aiznemts,lauc[2][2].aiznemts.krasa)
   """
      
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
    laukums.fill('chocolate')
    panelis2.fill('Red')
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
            for y in range(SpelesLaukumaIzmers-3, SpelesLaukumaIzmers):
                if matrica[x][y].krasa == Melns:
                    matrica[x][y].aiznemts = kaulins(Balts)

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

    def apkartejie(self, x, y):
        return [self.relativitate(KA, x, y), self.relativitate(LA, x, y), self.relativitate(KZ, x, y), self.relativitate(LZ, x, y)]
    

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
