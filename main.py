import pygame
import sys
from pygame.locals import *
from time import sleep

# speletaju krasas
#       R     G   B
Balts = (255, 255, 255)
Melns = (0,  0,  0)
fonakrasa = (37, 216, 85)
fons2krasa = (88, 206, 202)
iekrasots=(69,69,69)
# logu izmers
width = 800
height = 600

# speles iestatijumi
SpelesLaukumaIzmers = 12
kvadrataizmers = height/SpelesLaukumaIzmers

# Virzienu definicija
KA = "KA"  # kreisais augšejais
LA = "LA"  # labais augšējais
KZ = "KZ"  # Kreisais apakšejais/zemais
LZ = "LZ"  # Labais apakšējais/zemais

# PYGame iestatijumi
pygame.init()
pygame.display.set_caption('Dambrete')
clock = pygame.time.Clock()


def main():
    Running = True  # Mainigais ar kuru vares partraukt programams darbibu patraucot while loop

    spele = Spele()
    grf = spele.gr
    laukumavertibas1 = spele.galds1.atgriezt_laukumu()
    lauc = spele.galds1.matrica
    print("Arpus glada check=", spele.galds1.ArPusGalda(0, 2))
    print("Atlautie gajieni=", spele.galds1.atlautieGajieni(0, 2))
    print("vispariga kustiba=", spele.galds1.vienkarsakustiba(0, 2))
    spele.galds1.kustiba(0, 2, 1, 3)

    print("Atlautie gajieni=", spele.galds1.atlautieGajieni(1, 3))
    print("vispariga kustiba=", spele.galds1.vienkarsakustiba(1, 3))

    print("Atlautie gajieni=", spele.galds1.atlautieGajieni(1, 5))
    print("vispariga kustiba=", spele.galds1.vienkarsakustiba(1, 5))
    spele.galds1.kustiba(1, 5, 2, 4)
    print("Atlautie gajieni=", spele.galds1.atlautieGajieni(2, 4))
    print("vispariga kustiba=", spele.galds1.vienkarsakustiba(2, 4))
    spele.galds1.kustiba(2, 4, 0, 2)
    
    spele.galds1.matrica[1][3].aiznemts.dama = True
    while Running == True:
        grf.grafika()
        grf.krasojums()
       
        grf.grafKaul(lauc)
        pygame.display.update()
        spele.SpGajiens();
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Running = False
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                
                grf.iekrasoAtzimeto(spele.Gajieni,spele.atlasits)




#################################### SPeles grafikas saistitas funkcijas #############
class Grafika:
    def __init__(self):

        clock.tick(60)
        self.laukums = pygame.Surface((height, height))  # W H
        self.kvadra = pygame.Surface((kvadrataizmers, kvadrataizmers))  # W H
        self.kvadra.fill('white')
        self.panelis2 = pygame.Surface((width-height, height))
        self.font1 = pygame.font.Font(None, 50)
        self.screen = pygame.display.set_mode((width, height))
        self.teksts =  self.font1.render('Dambrete', False, 'black')
            # importe attelus un parveido to izmeru
        self.SP1att = pygame.image.load('atteli/speletajs1.png')
        self.SP2att = pygame.image.load('atteli/speletajs2.png')
        self.SP1datt = pygame.image.load('atteli/speletajs1dama.png')
        self.SP2datt = pygame.image.load('atteli/speletajs2dama.png')
        self.SP1att = pygame.transform.scale(
            self.SP1att, (kvadrataizmers, kvadrataizmers))
        self.SP2att = pygame.transform.scale(
            self.SP2att, (kvadrataizmers, kvadrataizmers))
        self.SP1datt = pygame.transform.scale(
            self.SP1datt, (kvadrataizmers, kvadrataizmers))
        self.SP2datt = pygame.transform.scale(
            self.SP2datt, (kvadrataizmers, kvadrataizmers))

    # iekrāso kvadrātu laukumus

    def krasojums(self):
        for x in range(SpelesLaukumaIzmers):
            for y in range(SpelesLaukumaIzmers):

                if (x % 2 != 0) and (y % 2 == 0):
                    self.screen.blit(
                        self.kvadra, (kvadrataizmers*x, kvadrataizmers*y))
                elif (x % 2 == 0) and (y % 2 != 0):
                    self.   screen.blit(
                        self.  kvadra, (kvadrataizmers*x, kvadrataizmers*y))

    def grafika(self):

        self.  screen.blit(self.laukums, (0, 0))
        self.  screen.blit(self.panelis2, (600, 0))
        self.  laukums.fill(fonakrasa)
        self.  panelis2.fill(fons2krasa)
        self. screen.blit(self.teksts, (600, 10))



# attelo kauliņus uz laukuma

    def grafKaul(self, matrica):
        for x in range(SpelesLaukumaIzmers):
            for y in range(SpelesLaukumaIzmers):
                if matrica[x][y].aiznemts != None:
                    if matrica[x][y].aiznemts.krasa == (255, 255, 255):
                        if not matrica[x][y].aiznemts.dama:
                            self. screen.blit(
                                self. SP1att, (kvadrataizmers*x, kvadrataizmers*y))
                        else:
                            self. screen.blit(
                                self.SP1datt, (kvadrataizmers*x, kvadrataizmers*y))
                    elif matrica[x][y].aiznemts.krasa == (0,  0,  0):
                        if not matrica[x][y].aiznemts.dama:
                            self. screen.blit(
                                self. SP2att, (kvadrataizmers*x, kvadrataizmers*y))
                        else:
                            self. screen.blit(
                                self. SP2datt, (kvadrataizmers*x, kvadrataizmers*y))
                    else:

                        pass
    def iekrasoAtzimeto(self,lauk,atzime):
        for lauki1 in lauk:
            pygame.draw.rect(self.screen,iekrasots,(lauki1[0]*kvadrataizmers,lauki1[1]*kvadrataizmers,kvadrataizmers,kvadrataizmers))
        if atzime !=None:
            pygame.draw.rect(self.screen,iekrasots,(atzime[0]*kvadrataizmers,atzime[1]*kvadrataizmers,kvadrataizmers,kvadrataizmers))                    


################################### speles gaitu saistitas funkcijas ######################
class Spele:
    """
    Speles sakums

    """

    def __init__(self):
        self.galds1 = Galds()
        self.gr = Grafika()
        self.atlasits = None
        self.speletajs = (255, 255, 255)
        self.lekt=False
        self.Gajieni=[]        
        
    # funkcija atgriez laucinu uzkura atrodas pele
    def lauks(self,x,y):
        return(x//kvadrataizmers,y//kvadrataizmers)
        
    def SpGajiens(self):
        Pele_pos = tuple(map(int, pygame.mouse.get_pos()))
        print(Pele_pos,"peles kordinates") #debug teksts prieks peles pozicijas noteiksanas
        self.peles_pos=tuple(map(int,self.lauks(Pele_pos[0],Pele_pos[1])))
        print(self.peles_pos," Pozicija laucina") #debug teksts prieks peles pozicijas noteiksanas
        if self.peles_pos[0]<SpelesLaukumaIzmers and self.peles_pos[1]<SpelesLaukumaIzmers:   
          if self.atlasits !=None:
                self.Gajieni=self.galds1.atlautieGajieni(self.atlasits[0],self.atlasits[1],self.lekt)
          if not self.lekt:
            a=self.galds1.lokacija(self.peles_pos[0],self.peles_pos[1])
            if a.aiznemts!=None and a.aiznemts.krasa==self.speletajs:
                  self.atlasits=self.peles_pos
            
            
        
       
       
       
    def beigas(self):
        skaitsW=0
        skaitsB-0
        flagW=False
        flagB=False
        for x in range(SpelesLaukumaIzmers):
               for y in range(SpelesLaukumaIzmers):
                   sp=self.galds1.lokacija(x,y)
                   if sp.krasa==Melns:
                       if sp.aiznemts!=None:
                        if self.galds1.lokacija(x,y).aiznemts.krasa == (255, 255, 255) :
                            skaitsW=skaitsW+1
                        else:
                            skaitsB=skaitsB+1
        if skaitsB==0:
            flagW=True
        if skaitsB==0:
            flagB=True
        if flagB==True or flagW==True:
            return True
        else:
            return False            
                    
       
       
       
################################################## Speles galdu saistitas funkcijas #############################
class Galds:
    def __init__(self):
        self.matrica = self.jaunaSpele()

    def jaunaSpele(self):
        # izveido jaunu laukumu
        
        matrica = [[None]*SpelesLaukumaIzmers for i in range(SpelesLaukumaIzmers)]
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
                    # print(x,y,"melns") #printe kaulinu izvietojumu speles sakuma
            for y in range(SpelesLaukumaIzmers-3, SpelesLaukumaIzmers):
                if matrica[x][y].krasa == Melns:
                    matrica[x][y].aiznemts = kaulins(Balts)
                    # print(x,y,"balts") #printe kaulinu izvietojumu speles sakuma

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
    # atgriez apkartejos laucinuss

    def apkartejie(self, x, y):
        return [self.relativitate(KA, x, y), self.relativitate(LA, x, y), self.relativitate(KZ, x, y), self.relativitate(LZ, x, y)]
    # atgriez visus gajienus kaulinam

    def vienkarsakustiba(self, x, y):

        if self.matrica[x][y].aiznemts != None:
            if self.matrica[x][y].aiznemts.dama == False and self.matrica[x][y].aiznemts.krasa == (255, 255, 255):
                gajiens = [self.relativitate(
                    KA, x, y), self.relativitate(LA, x, y)]
            elif self.matrica[x][y].aiznemts.dama == False and self.matrica[x][y].aiznemts.krasa == (0, 0, 0):
                gajiens = [self.relativitate(
                    KZ, x, y), self.relativitate(LZ, x, y)]
            else:
                gajiens = [self.relativitate(KZ, x, y), self.relativitate(
                    LZ, x, y), self.relativitate(KA, x, y), self.relativitate(LA, x, y)]
        else:
            gajiens = []

        return gajiens
    # parbauda vai kordinate arpus galda

    def ArPusGalda(self, x, y):
        if x < 0 or y < 0 or x >= SpelesLaukumaIzmers or y >= SpelesLaukumaIzmers:
            return True
        else:
            return False
    # Aizvieto kaulinu at tukšu vietu.

    def NonemtKaulinu(self, x, y):
        self.matrica[x][y].aiznemts = None
    # Veic Kustību

    def kustiba(self, x0, y0, x1, y1):
        m = self.matrica
        m[x1][y1].aiznemts = m[x0][y0].aiznemts
        self.NonemtKaulinu(x0, y0)
        self.kronet(x1, y1)
    # atgriez atlautos gajienus

    def atlautieGajieni(self, x, y, lekt=False):
        # vk- vienkarsa kustiba | AG- atlautie gajieni|  ga- gajiens | m matrica | mat - matrica ar kordinatem no gajiena
        m = self.matrica
        VK = self.vienkarsakustiba(x, y)
        AG = []
        if not lekt:
            for ga in VK:
                if not self.ArPusGalda(ga[0], ga[1]):
             
                    if m[ga[0]][ga[1]].aiznemts == None:
                        AG.append(ga)
                    elif m[ga[0]][ga[1]].aiznemts.krasa != m[x][y].aiznemts.krasa and not self.ArPusGalda(ga[0]+(ga[0]-x), ga[1]+(ga[1]-y)) and m[ga[0]+(ga[0]-x)][ga[1]+(ga[1]-y)].aiznemts == None:
                        AG.append((ga[0]+(ga[0]-x), ga[1]+(ga[1]-y)))
        else:
            for ga in VK:
                if not self.ArPusGalda(ga[0], ga[1]):
                    if m[ga[0]][ga[1]].aiznemts == None:
                        if m[ga[0]][ga[1]].aiznemts.krasa != m[x][y].aiznemts.krasa and not self.ArPusGalda(ga[0]+(ga[0]-x), ga[1]+(ga[1]-y)) and m[ga[0]+(ga[0]-x)][ga[1]+(ga[1]-y)].aiznemts == None:
                            AG.append((ga[0]+(ga[0]-x), ga[1]+(ga[1]-y)))
        return AG

    def kronet(self, x, y):
        if self.matrica[x][y].aiznemts != None:
            if (self.matrica[x][y].aiznemts.krasa == (255, 255, 255) and y == 0) or (self.matrica[x][y].aiznemts.krasa == (0, 0, 0) and y == SpelesLaukumaIzmers):
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



########################################## Bota funkcijas #########################################
#To be added 
class Bots:
    def __init__(self) -> None:
        pass






######################################## INICIALIZE MAIN FUNKCIJU #################################################
if __name__ == "__main__":
    main()
    pass
