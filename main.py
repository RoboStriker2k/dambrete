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
SpelesLaukumaIzmers = 7 # maina speles laukuma lielumu ( domats rindu un kolonu skaits)
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
    #laukumavertibas1 = spele.galds1.atgriezt_laukumu()
   
    # print("Arpus glada check=", spele.galds1.ArPusGalda(0, 2))
    # print("Atlautie gajieni=", spele.galds1.atlautieGajieni(0, 2))
    # print("vispariga kustiba=", spele.galds1.vienkarsakustiba(0, 2))
    # spele.galds1.kustiba(0, 2, 1, 3)

    # print("Atlautie gajieni=", spele.galds1.atlautieGajieni(1, 3))
    # print("vispariga kustiba=", spele.galds1.vienkarsakustiba(1, 3))

    # print("Atlautie gajieni=", spele.galds1.atlautieGajieni(1, 5))
    # print("vispariga kustiba=", spele.galds1.vienkarsakustiba(1, 5))
    # spele.galds1.kustiba(1, 5, 2, 4)
    # print("Atlautie gajieni=", spele.galds1.atlautieGajieni(2, 4))
    # print("vispariga kustiba=", spele.galds1.vienkarsakustiba(2, 4))
    # spele.galds1.kustiba(2, 4, 0, 2)
    
    # spele.galds1.matrica[1][3].aiznemts.dama = True
    while Running == True:
        grf.update(spele)
    
        # grf.grafika()
        # grf.krasojums()
        # grf.grafKaul(spele.galds1.matrica)
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Running = False
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
             #   print(spele.Gajieni,spele.atlasits,"Pirms")
                spele.SpGajiens()
               # print(spele.Gajieni,spele.atlasits,"pec")
                
              #  print(spele.Gajieni,spele.atlasits,"Talak")
                pygame.display.update()
                if spele.beigas()==True:
                        spele=Spele()

            if event.type==pygame.KEYDOWN and event.key==pygame.K_g:
                    spele.mainispeletaju()
                   
                


#################################### SPeles grafikas saistitas funkcijas #############
class Grafika:
    def __init__(self):

        clock.tick(10)
        self.laukums = pygame.Surface((height, height))  # W H
        self.kvadra = pygame.Surface((kvadrataizmers, kvadrataizmers))
        self.kvadra2 = pygame.Surface((kvadrataizmers, kvadrataizmers)) # W H
        
        self.panelis2 = pygame.Surface((width-height, height))
        self.font1 = pygame.font.Font(None, 50)
        self.font2 = pygame.font.Font(None, 25)
        self.screen = pygame.display.set_mode((width, height))
        self.teksts =  self.font1.render('Dambrete', False, 'black')
        self.teksts2=self.font2.render('Speletaja Vertiba=',False,'black')
        
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
    def update(self,spe):
        self.grafika()
        self.krasojums()
        self.attelovertibu(spe.SpeletajaVertiba())
        
        if spe.atlasits !=None:
            self.iekrasoAtzimeto(spe.galds1.atlautieGajieni(spe.atlasits[0],spe.atlasits[1]),spe.atlasits)
        self.grafKaul(spe.galds1.matrica)    
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
        self.screen.blit(self.laukums, (0, 0))
        self.screen.blit(self.panelis2, (600, 0))
        self.laukums.fill(fonakrasa)
        self.panelis2.fill(fons2krasa)
        self.screen.blit(self.teksts, (600, 10))
        self.screen.blit(self.teksts2, (600, 50))
        self.kvadra.fill('white')
        self.kvadra2.fill(iekrasots)

   


    def grafKaul(self, matrica):# attelo kauliņus uz laukuma
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
        if lauk!=None:
         for lauki1 in lauk:
            self. screen.blit( self. kvadra2 ,(lauki1[0]*kvadrataizmers,lauki1[1]*kvadrataizmers))
        if atzime !=None:
           self. screen.blit(self. kvadra2,(atzime[0]*kvadrataizmers,atzime[1]*kvadrataizmers))                    
    def attelovertibu(self,vertiba):
        vertiba=str(vertiba)
        self.teksts3=self.font2.render(vertiba,False,'black')
        self.screen.blit(self.teksts3, (780, 50))

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
        
    def mainispeletaju(self):
        if self.speletajs==(255, 255, 255):
            self.speletajs=(0, 0, 0)
        else:
            self.speletajs=(255, 255, 255)
    def lauks(self,x,y):   # funkcija atgriez laucinu uzkura atrodas pele
        return(x//kvadrataizmers,y//kvadrataizmers)
        
    def SpGajiens(self):
        Pele_pos = tuple(map(int, pygame.mouse.get_pos()))
      #  print(Pele_pos,"peles kordinates") #debug teksts prieks peles pozicijas noteiksanas
        self.peles_pos=tuple(map(int,self.lauks(Pele_pos[0],Pele_pos[1])))
      #  print(self.peles_pos," Pozicija laucina") #debug teksts prieks peles pozicijas noteiksanas
        if self.peles_pos[0]<SpelesLaukumaIzmers and self.peles_pos[1]<SpelesLaukumaIzmers:   
          if self.atlasits !=None:
            self.Gajieni=self.galds1.atlautieGajieni(self.atlasits[0],self.atlasits[1],self.lekt)
          if not self.lekt:
            a=self.galds1.lokacija(self.peles_pos[0],self.peles_pos[1])
            if a.aiznemts!=None and a.aiznemts.krasa==self.speletajs:
                  self.atlasits=self.peles_pos
            elif self.atlasits!= None and self.peles_pos in self.galds1.atlautieGajieni(self.atlasits[0],self.atlasits[1]):
                self.galds1.kustiba(self.atlasits[0],self.atlasits[1],self.peles_pos[0],self.peles_pos[1])
                if self.peles_pos not in self.galds1.apkartejie(self.atlasits[0],self.atlasits[1]):
                        self.galds1.NonemtKaulinu(self.atlasits[0] + (self.peles_pos[0] - self.atlasits[0]) // 2, self.atlasits[1] + (self.peles_pos[1] - self.atlasits[1]) // 2)
                        self.lekt=True
                        self.atlasits=self.peles_pos
                        
                else:
                    self.BeigtGajienu()
        if self.lekt:
            if self.atlasits!= None and self.peles_pos in self.galds1.atlautieGajieni(self.atlasits[0],self.atlasits[1],self.lekt):
                self.galds1.kustiba(self.atlasits[0],self.atlasits[1],self.peles_pos[0],self.peles_pos[1])
                self.galds1.NonemtKaulinu(self.atlasits[0] + (self.peles_pos[0] - self.atlasits[0]) // 2, self.atlasits[1] + (self.peles_pos[1] - self.atlasits[1]) // 2)
            if self.galds1.atlautieGajieni(self.peles_pos[0],self.peles_pos[1],self.lekt)==[]:
                self.BeigtGajienu()
            else:
                self.atlasits=self.peles_pos              
       
    def BeigtGajienu(self) :
        if self.speletajs==(255, 255, 255):
            self.speletajs=(0, 0, 0)
        else:
            self.speletajs=(255, 255, 255)
            
        self.atlasits=None
        self.Gajieni=None
        self.lekt=False    
          
       
    def beigas(self):
        skaitsW=0
        skaitsB=0
        flagW=False
        flagB=False
        for x in range(SpelesLaukumaIzmers):
               for y in range(SpelesLaukumaIzmers):
                   sp=self.galds1.lokacija(x,y)
                   if sp.krasa==Melns:
                       if sp.aiznemts!=None:
                        if self.galds1.lokacija(x,y).aiznemts.krasa == (255, 255, 255) :
                            skaitsW=skaitsW+1

                        elif self.galds1.lokacija(x,y).aiznemts.krasa == (0, 0, 0) :
                            skaitsB=skaitsB+1
        if skaitsW==0:
            flagW=True
        if skaitsB==0:
            flagB=True
        if flagB or flagW:
            return True
        else:
            return False            
    def SpeletajaVertiba(self):
        skaits=0   
        for x in range(SpelesLaukumaIzmers):
               for y in range(SpelesLaukumaIzmers):
                   sp=self.galds1.lokacija(x,y)
                   if sp.krasa==Melns:
                       if sp.aiznemts!=None:
                           
                        if sp.aiznemts.krasa == self.speletajs :
                            skaits=skaits+ sp.aiznemts.vertiba
                           
        return skaits
  
         
################################################## Speles galdu saistitas funkcijas #############################
class Galds:
    def __init__(self):
        self.matrica = self.jaunaSpele()
    def jaunaSpele(self):
        # izveido jaunu laukumu
        matrica = [[None]*SpelesLaukumaIzmers for i in range(SpelesLaukumaIzmers)]
        for x in range(SpelesLaukumaIzmers): # azipilda to ar lauciņiem
            for y in range(SpelesLaukumaIzmers):
                if ((x % 2 > 0) and (y % 2 == 0)) or ((x % 2 == 0) and (y % 2 > 0)):
                    matrica[x][y] = laucins(Balts)
                elif ((x % 2 > 0) and (y % 2 > 0)) or ((x % 2 == 0) and (y % 2 == 0)):
                    matrica[x][y] = laucins(Melns)

        
        for x in range(SpelesLaukumaIzmers):# aizpilda to ar kauliņiem
            for y in range(3):
                if matrica[x][y].krasa == Melns:
                    matrica[x][y].aiznemts = kaulins(Melns)
                    # print(x,y,"melns") #printe kaulinu izvietojumu speles sakuma
            for y in range(SpelesLaukumaIzmers-3, SpelesLaukumaIzmers):
                if matrica[x][y].krasa == Melns:
                    matrica[x][y].aiznemts = kaulins(Balts)
                    # print(x,y,"balts") #printe kaulinu izvietojumu speles sakuma

        return matrica


    def lokacija(self, x, y):# atgriez matricas elementu 
        return self.matrica[x][y]
    
    def relativitate(self, virziens, x, y):#atgriez apkartejo laukumu kordināti
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
    

    def apkartejie(self, x, y):# atgriez apkartejos laucinuss
        return [self.relativitate(KA, x, y), self.relativitate(LA, x, y), self.relativitate(KZ, x, y), self.relativitate(LZ, x, y)]

    def vienkarsakustiba(self, x, y):# atgriez visus gajienus kaulinam
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
    

    def ArPusGalda(self, x, y):# parbauda vai kordinate arpus galda #ja x,y vienads ar SpelesLaukumaIzmeru matrica[x][y]atgriez out of index
        if x < 0 or y < 0 or x >= SpelesLaukumaIzmers or y >= SpelesLaukumaIzmers:
            return True
        else:
            return False
    def NonemtKaulinu(self, x, y): # Aizvieto kaulinu at tukšu vietu.
        self.matrica[x][y].aiznemts = None
    def kustiba(self, x0, y0, x1, y1):# Veic Kustību
        m = self.matrica
        m[x1][y1].aiznemts = m[x0][y0].aiznemts
        self.NonemtKaulinu(x0, y0)
        self.kronet(x1, y1)
    def atlautieGajieni(self, x, y, lekt=False):# atgriez atlautos gajienus
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
                    if m[ga[0]][ga[1]].aiznemts != None:
                        if m[ga[0]][ga[1]].aiznemts.krasa != m[x][y].aiznemts.krasa and not self.ArPusGalda(ga[0]+(ga[0]-x), ga[1]+(ga[1]-y)) and m[ga[0]+(ga[0]-x)][ga[1]+(ga[1]-y)].aiznemts == None:
                            AG.append((ga[0]+(ga[0]-x), ga[1]+(ga[1]-y)))
       # print(AG,"-Atlautie gajieni")
        return AG

    def kronet(self, x, y):
        if self.matrica[x][y].aiznemts != None:
            if (self.matrica[x][y].aiznemts.krasa == (255, 255, 255) and y == 0) or (self.matrica[x][y].aiznemts.krasa == (0, 0, 0) and y == SpelesLaukumaIzmers-1):
                self.matrica[x][y].aiznemts.damas()

######################################## Kaulina definicija ############################################
class kaulins:
    def __init__(self, krasa, dama=False):
        self.krasa = krasa
        self.dama = dama
        self.vertiba = 1
    def damas(self):
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
    def __init__(self,spele,krasa,dzilums=1) :
       self.dzilums=dzilums
       self.spele=spele
       self.krasa=krasa
       self.parbaudamais=krasa
    def minmax(self,dzilums,spele,speletajs):
        if dzilums==0:
            if speletajs=='max':
                pass



####################### speles koka virsotne #########
class Virsotne:
    def __init__(self, id, gajieni, p1, p2, limenis) :
        self.id=id
        self.gajieni=gajieni
        self.p1=p1
        self.p2=p2
        self.limenis=limenis
##################### Speles koks ##################
class SpelesKoks:
    def __init__(self):
        self.virstones=[]
        self.loki=dict()        
    def PievienoVirsotni(self,Virstone):
        self.virstones.append(Virsotne)
    def PievienoLoku(self,svirsotne,bvirsotne):
        self.loki[svirsotne]=self.loki.get(svirsotne,[])+[bvirsotne]    




######################################## INICIALIZE MAIN FUNKCIJU #################################################
if __name__ == "__main__":
    main()
    pass
