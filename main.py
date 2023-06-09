import pygame
import sys
from pygame.locals import *
import math
from copy import deepcopy  # galda kopešana
import time 
# speletaju krasas
#       R     G   B
Balts = (255, 255, 255)
Melns = (0,  0,  0)
fonakrasa = (37, 216, 85)
fons2krasa = (88, 206, 202)
iekrasots = (69, 69, 69)

# logu izmers
height = 600  # loga augstums, izmatots gan lauku grafikai gan citas vietas
width = height+200
# speles iestatijumi
# maina speles laukuma lielumu ( domats rindu un kolonu skaits) # min 7 
SpelesLaukumaIzmers = 8
# Laukumu kvadrātu izmērs | lietots gan grafikai, gan saskarsmei.
kvadrataizmers = height/SpelesLaukumaIzmers

# Virzienu definicija
KA = "KA"  # kreisais augšejais
LA = "LA"  # labais augšējais
KZ = "KZ"  # Kreisais apakšejais/zemais
LZ = "LZ"  # Labais apakšējais/zemais

# PYGame iestatijumi
pygame.init()
pygame.display.set_caption('Dambrete')
screen = pygame.display.set_mode((width, height))
laukums = pygame.Surface((height, height))  # W H
kvadra = pygame.Surface((kvadrataizmers, kvadrataizmers))
kvadra2 = pygame.Surface((kvadrataizmers, kvadrataizmers))  # W H
panelis2 = pygame.Surface((width-height, height))
#izmantotie fonti
font1 = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 25)
clock = pygame.time.Clock()
#teksts kas tiek rādits grafiskaja vide
teksts = font1.render('Dambrete', False, 'black')
teksts2 = font2.render('Speletaja Vertiba=', False, 'black')
teksts4 = font2.render('Poga G - mainit pusi', False, 'black')
teksts5 = font2.render('Poga h - reset laukums', False, 'black')
teksts6 = font2.render('Poga 0- 1v1 No bot', False, 'black')
teksts7 = font2.render('Poga 1- 1v1 Ar bot', False, 'black')
teksts8 = font2.render('Poga 2- 1v1 Abi bot', False, 'black')
# importe attelus un parveido to izmeru
SP1att = pygame.image.load('atteli/speletajs1.png')
SP2att = pygame.image.load('atteli/speletajs2.png')
SP1datt = pygame.image.load('atteli/speletajs1dama.png')
SP2datt = pygame.image.load('atteli/speletajs2dama.png')
SP1att = pygame.transform.scale(SP1att, (kvadrataizmers, kvadrataizmers))
SP2att = pygame.transform.scale(SP2att, (kvadrataizmers, kvadrataizmers))
SP1datt = pygame.transform.scale(SP1datt, (kvadrataizmers, kvadrataizmers))
SP2datt = pygame.transform.scale(SP2datt, (kvadrataizmers, kvadrataizmers))
##########################################################################



def DecodeBotaReturn(teksts):
    #reizem atgriez atbildi par isu, kad nav vertibu 
    pir = teksts[0]
    gajiens = (pir[0], pir[1])
    # atgriez visu nepieciesamo virsotnei
    print(gajiens, pir[2], teksts[1], teksts[2])
    return gajiens, pir[2], teksts[1], teksts[2]


def main():
    Running = True  # Mainigais ar kuru vares partraukt programams darbibu patraucot while loop
    spele = Spele()  # inicializeta kalse spele kura tiks izmantota speles darbibas  gaita
    grf = spele.gr  # ar grafiku saistita apstrade kura izsauc speles izsaukto grafikas klasi
    ArBotu = 0 # mainigais ar kuru kontrole cik botu # 0 - nav # 1 - viens # 2 -divi
    while Running == True:
        if ArBotu == 0:
           # Speles galvenais cikls Bez Algoritma, diviem speletajiem katram nemot gajienu
            grf.update(spele)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    Running = False
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    spele.SpGajiens()
                    pygame.display.update()
                    if spele.beigas() == True:
                        spele = Spele()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                    spele.mainispeletaju()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                        spele.galds.__init__()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                        ArBotu=0
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                        ArBotu=1
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                        ArBotu=2              
        elif ArBotu == 1:
            vertiba = 0
            spele2 = deepcopy(spele)
            bots = Bots(spele2, (0,  0,  0), 8)
            if spele.speletajs == Balts:     
                    bots.gajiens(spele)
                    vertiba = bots.VertejumsGalda(spele)
                    spele.speletajs=Melns
            time.sleep(0.1)
            grf.update(spele)
            grf.attelovertibu(vertiba)
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
                        if spele.beigas() == True:
                            spele = Spele()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                        spele.mainispeletaju()
                    
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                        spele.galds.__init__()            
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                        ArBotu=0
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                        ArBotu=1
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                        ArBotu=2    
                         
    # Speles galvenais cikls   Ar algoritma implementāciju abiem speletajiem
        else:
      
            vertiba = 0
            spele2 = deepcopy(spele)
            if spele.speletajs == Melns:
                    bots = Bots(spele2, (0,  0,  0), 3)
                    if not bots.gajiens(spele):
                        ArBotu=0
                    vertiba = bots.VertejumsGalda(spele)
            else:
                    bots2 = Bots(spele2, (255,  255, 255), 3)
                    if not bots2.gajiens(spele):
                        ArBotu=0
                    vertiba = bots2.VertejumsGalda(spele)
            time.sleep(0.01)
            grf.update(spele)
            grf.attelovertibu(vertiba)
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
                        if spele.beigas() == True:
                            spele = Spele()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                        spele.mainispeletaju()

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                        spele.galds.__init__()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_0:
                        ArBotu=0
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                        ArBotu=1
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                        ArBotu=2  

#################################### SPeles grafikas saistitas funkcijas #############
class Grafika:
    def __init__(self):

        clock.tick(60)

    # iekrāso kvadrātu laukumus

    def update(self, spe):# funkcija prieks laukumu krasojumu izsaukšanas
        self.grafika()
        self.krasojums()

        if spe.atlasits != None:
            self.iekrasoAtzimeto(spe.galds.atlautieGajieni(
                spe.atlasits[0], spe.atlasits[1]), spe.atlasits)
        self.grafKaul(spe.galds.matrica)

    def krasojums(self):    #Iekrāso krāsainos laukus uz speles laukuma
        for x in range(SpelesLaukumaIzmers):
            for y in range(SpelesLaukumaIzmers):

                if (x % 2 != 0) and (y % 2 == 0):
                    screen.blit(
                        kvadra, (kvadrataizmers*x, kvadrataizmers*y))
                elif (x % 2 == 0) and (y % 2 != 0):
                    screen.blit(
                        kvadra, (kvadrataizmers*x, kvadrataizmers*y))

    def grafika(self): #lielākā daļa no krasojamiem objektiem uz pygame loga
        screen.blit(laukums, (0, 0))
        screen.blit(panelis2, (600, 0))
        laukums.fill(fonakrasa)
        panelis2.fill(fons2krasa)
        screen.blit(teksts, (600, 10))
        screen.blit(teksts2, (600, 50))
        kvadra.fill('white')
        kvadra2.fill(iekrasots)
        screen.blit(teksts4, (600, 100))
        screen.blit(teksts5, (600, 200))
        screen.blit(teksts6, (600, 250))
        screen.blit(teksts7, (600, 300))
        screen.blit(teksts8, (600, 350))

    def grafKaul(self, matrica):  # attelo kauliņus uz laukuma izzejot cauri matricas elementiem, ja atrod tad iezīmē
        for x in range(SpelesLaukumaIzmers):
            for y in range(SpelesLaukumaIzmers):
                if matrica[x][y].aiznemts != None:
                    if matrica[x][y].aiznemts.krasa == (255, 255, 255):
                        if not matrica[x][y].aiznemts.dama:
                            screen.blit(
                                SP1att, (kvadrataizmers*x, kvadrataizmers*y))
                        else:
                            screen.blit(
                                SP1datt, (kvadrataizmers*x, kvadrataizmers*y))
                    elif matrica[x][y].aiznemts.krasa == (0,  0,  0):
                        if not matrica[x][y].aiznemts.dama:
                            screen.blit(
                                SP2att, (kvadrataizmers*x, kvadrataizmers*y))
                        else:
                            screen.blit(
                                SP2datt, (kvadrataizmers*x, kvadrataizmers*y))
                    else:

                        pass

    def iekrasoAtzimeto(self, lauk, atzime): #iekrāso atlasīto lauku un laukus kuri ir pieejami ka nakamie gajieni
        if lauk != None:
            for lauki1 in lauk:
                screen.blit(
                    kvadra2, (lauki1[0]*kvadrataizmers, lauki1[1]*kvadrataizmers))
        if atzime != None:
            screen.blit(
                kvadra2, (atzime[0]*kvadrataizmers, atzime[1]*kvadrataizmers))

    def attelovertibu(self, vertiba): #Attēlo vērtibu pie Speletāja veriba uzraksta
        vertiba = str(vertiba)
        teksts3 = font2.render(vertiba, False, 'black')
        screen.blit(teksts3, (760, 50))

################################### speles gaitu saistitas funkcijas ######################


class Spele:
    def __init__(self):
        self.galds = Galds()  # apzime galda mainigo
        self.gr = Grafika()  # apzime grafikas klases mainigo
        self.atlasits = None  # atlausita laucina vertiba
        self.speletajs = (255, 255, 255)  # tagadeja speletaja vertiba
        self.lekt = False  # vertiba ja var lekt pari
        self.Gajieni = []  # Atlauto gajienu matrica

    def AtgrieztGaldaKopiju(self):
        #neizmantota funkcija galda kopešanai
        gald = deepcopy(self.galds)
        return gald

    def mainispeletaju(self):
        #funkcija ar kuru izmantojot g pogu iespejams mainīt spēlētāja pusi pašam 
        if self.speletajs == (255, 255, 255):
            self.speletajs = (0, 0, 0)
        else:
            self.speletajs = (255, 255, 255)

    def lauks(self, x, y):   # funkcija atgriez laucinu uzkura atrodas pele 
        #tas ir x pixel / kvadrāta izmers  piezemināts pie vesela skaitļa 
        return (x//kvadrataizmers, y//kvadrataizmers)

    def SpGajiens(self):
        #funkcija spēlētāja gājienam.
        Pele_pos = tuple(map(int, pygame.mouse.get_pos()))
      #  print(Pele_pos,"peles kordinates") #debug teksts prieks peles pozicijas noteiksanas
        self.peles_pos = tuple(map(int, self.lauks(Pele_pos[0], Pele_pos[1])))
      #  print(self.peles_pos," Pozicija laucina") #debug teksts prieks peles pozicijas noteiksanas
        if self.peles_pos[0] < SpelesLaukumaIzmers and self.peles_pos[1] < SpelesLaukumaIzmers:
            if self.atlasits != None:
                self.Gajieni = self.galds.atlautieGajieni(
                    self.atlasits[0], self.atlasits[1], self.lekt)
            if not self.lekt:
                a = self.galds.lokacija(self.peles_pos[0], self.peles_pos[1])
                if a.aiznemts != None and a.aiznemts.krasa == self.speletajs:
                    self.atlasits = self.peles_pos
                elif self.atlasits != None and self.peles_pos in self.galds.atlautieGajieni(self.atlasits[0], self.atlasits[1]):
                    self.galds.kustiba(
                        self.atlasits[0], self.atlasits[1], self.peles_pos[0], self.peles_pos[1])
                    if self.peles_pos not in self.galds.apkartejie(self.atlasits[0], self.atlasits[1]):
                        self.galds.NonemtKaulinu(
                            self.atlasits[0] + (self.peles_pos[0] - self.atlasits[0]) // 2, self.atlasits[1] + (self.peles_pos[1] - self.atlasits[1]) // 2)
                        self.lekt = True
                        self.atlasits = self.peles_pos

                    else:
                        self.BeigtGajienu()
        if self.lekt:
            if self.atlasits != None and self.peles_pos in self.galds.atlautieGajieni(self.atlasits[0], self.atlasits[1], self.lekt):
                self.galds.kustiba(
                    self.atlasits[0], self.atlasits[1], self.peles_pos[0], self.peles_pos[1])
                self.galds.NonemtKaulinu(self.atlasits[0] + (self.peles_pos[0] - self.atlasits[0]) //
                                         2, self.atlasits[1] + (self.peles_pos[1] - self.atlasits[1]) // 2)
            if self.galds.atlautieGajieni(self.peles_pos[0], self.peles_pos[1], self.lekt) == []:
                self.BeigtGajienu()
            else:
                self.atlasits = self.peles_pos

    def BeigtGajienu(self):
        #Funkcija gajiena beigšanai, speletāja nomaiņai
        if self.speletajs == (255, 255, 255):
            self.speletajs = (0, 0, 0)
        else:
            self.speletajs = (255, 255, 255)

        self.atlasits = None
        self.Gajieni = None
        self.lekt = False

    def beigas(self):
        #veic parbaudi vai viena no pusēm ir bez kauliņiem
        skaitsW = 0
        skaitsB = 0
        flagW = False
        flagB = False
        for x in range(SpelesLaukumaIzmers):
            for y in range(SpelesLaukumaIzmers):
                sp = self.galds.lokacija(x, y)
                if sp.krasa == Melns:
                    if sp.aiznemts != None:
                        if self.galds.lokacija(x, y).aiznemts.krasa == (255, 255, 255):
                            skaitsW = skaitsW+1

                        elif self.galds.lokacija(x, y).aiznemts.krasa == (0, 0, 0):
                            skaitsB = skaitsB+1
        if skaitsW == 0:
            flagW = True
        if skaitsB == 0:
            flagB = True
        if flagB or flagW:
            return True
        else:
            return False


################################################## Speles galdu saistitas funkcijas #############################
class Galds:
    def __init__(self):
        self.matrica = self.jaunaSpele()

    def jaunaSpele(self):
        # izveido jaunu laukumu Spelei
        matrica = [
            [None]*SpelesLaukumaIzmers for i in range(SpelesLaukumaIzmers)]
        for x in range(SpelesLaukumaIzmers):  # azipilda to ar lauciņiem
            for y in range(SpelesLaukumaIzmers):
                if ((x % 2 > 0) and (y % 2 == 0)) or ((x % 2 == 0) and (y % 2 > 0)):
                    matrica[x][y] = laucins(Balts)
                elif ((x % 2 > 0) and (y % 2 > 0)) or ((x % 2 == 0) and (y % 2 == 0)):
                    matrica[x][y] = laucins(Melns)

        for x in range(SpelesLaukumaIzmers):  # aizpilda to ar kauliņiem
            for y in range(3):
                if matrica[x][y].krasa == Melns:
                    matrica[x][y].aiznemts = kaulins(Melns)
                    # print(x,y,"melns") #printe kaulinu izvietojumu speles sakuma
            for y in range(SpelesLaukumaIzmers-3, SpelesLaukumaIzmers):
                if matrica[x][y].krasa == Melns:
                    matrica[x][y].aiznemts = kaulins(Balts)
                    # print(x,y,"balts") #printe kaulinu izvietojumu speles sakuma

        return matrica

    def lokacija(self, x, y):  # atgriez matricas elementu #parasti tas ir kaulina objekts vai None
        return self.matrica[x][y]

    def relativitate(self, virziens, x, y):  # atgriez apkartejo laukumu kordināti
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

    def apkartejie(self, x, y):  # atgriez apkartejos laucinuss pa diogonāli
        return [self.relativitate(KA, x, y), self.relativitate(LA, x, y), self.relativitate(KZ, x, y), self.relativitate(LZ, x, y)]

    def vienkarsakustiba(self, x, y):  # atgriez visus gajienus kaulinam, kas atļauti
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

    # parbauda vai kordinate arpus galda #ja x,y vienads ar SpelesLaukumaIzmeru matrica[x][y]atgriez out of index
    def ArPusGalda(self, x, y):
        if x < 0 or y < 0 or x >= SpelesLaukumaIzmers or y >= SpelesLaukumaIzmers:
            return True
        else:
            return False

    def NonemtKaulinu(self, x, y):  # Aizvieto kaulinu at tukšu vietu.
        self.matrica[x][y].aiznemts = None

    def kustiba(self, x0, y0, x1, y1):  # Veic Kustību Uz speles galda
        m = self.matrica
        m[x1][y1].aiznemts = m[x0][y0].aiznemts
        self.NonemtKaulinu(x0, y0)
        self.kronet(x1, y1)

    def atlautieGajieni(self, x, y, lekt=False):  # atgriez atlautos gajienus
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
        #funkcija padara kaulinu par dāmu 
        if self.matrica[x][y].aiznemts != None:
            if (self.matrica[x][y].aiznemts.krasa == (255, 255, 255) and y == 0) or (self.matrica[x][y].aiznemts.krasa == (0, 0, 0) and y == SpelesLaukumaIzmers-1):
                self.matrica[x][y].aiznemts.damas() 

######################################## Kaulina definicija ############################################


class kaulins:
    def __init__(self, krasa, dama=False):
        self.krasa = krasa #vertiba ar kuru atspogulo kaulina krasu 
        self.dama = dama #vertiba ar kuru atspogulo vai ir dama
        self.vertiba=1 #neizmantota vertiba jo neizmanto kaulvertibas funkciju
    def damas(self): #funkcija ar kuru maina vertibu kauliņam
        self.dama = True #vertiba ar kuru atspogulo vai ir dama
        self.vertiba=2 #neizmantota vertiba jo neizmanto kaulvertibas funkciju
######################################### Laucina definicija  ##########################################


class laucins:
    def __init__(self, krasa, aiznemts=None):
        self.krasa = krasa         #krasa laucinam BALTA VAI MELNA
        self.aiznemts = aiznemts    #VAI LAUCINS AIZNEMTS JA AIZNEMTS TAD AR KAULINA KLASES OBJEKTU


########################################## Bota funkcijas #########################################
# To be added
class Bots:
    def __init__(self, spele, krasa, dzilums=1):
        self.dzilums = dzilums #saglabā dziluma vertibu lidz kura tiek apskatīti gajieni
        self.spele = spele  #speles mainigais kuru parsti tapat nododu ka parametru funkcijai , Lieks
        self.krasa = krasa  #Datora speletaja krasa
        self.pretineika = krasa #Pretinieka speletaja krasa
        self.parbaudamakrasa = krasa #Datora speletaja krasa lieka, gandriz neizmantoju
        if self.krasa == (255, 255, 255):
            self.pretineika = (0, 0, 0)
        else:
            self.pretineika = (255, 255, 255)
            
    def gajiens(self,spele): #funckijas kas izsauc minmax gajiena funkciju
        if self.VaiVelIrParastie==False:
            print('Iestrega Ar Visam damam') 
            return False  
        if self.minimaxGajiens(spele):
            return True
        else: return False       
    def minimaxGajiens(self,spele):
        #funkcija kas izmantota minmax algoritma izsaukšānai un gajiena veikšanai
        spele2 = deepcopy(spele) #izveido spēles mainigajam pilnīgu kopiju
        huh=self.minmax(self.dzilums,spele2,'max') 
        #print (huh)
        if huh is None:
            return False
        LabakaPos,  LabakaisGajiens,vertiba= huh
        
        self.VeiktGajienu(spele,LabakaPos,LabakaisGajiens)
        return True
    def minmax(self, dzilums, spele, Speletajs):
        #funkcija kas veido minmax algoritmu
        # zem speletājs domāts min or max gajiens
        if dzilums <= 0:
            if Speletajs == 'max':
                vertiba = -math.inf
                LabakaPos = None
                LabakaisGajiens = None
                Iespejamie_Gajieni = self.GajienuIegusana(spele)
                for gajieni in Iespejamie_Gajieni:
                    #  print(gajieni)
                    for lauks in gajieni[2]:
                        # print(lauks)
                        self.krasa, self.pretineika = self.pretineika, self.krasa
                        spele.speletajs = self.krasa
                        self.VeiktGajienu(spele, gajieni, lauks)
                        gajienavertiba = self.VertejumsGalda(spele)
                        if gajienavertiba > vertiba:
                            vertiba = gajienavertiba
                            LabakaPos = gajieni
                            LabakaisGajiens = (lauks[0], lauks[1])
                        elif gajienavertiba == vertiba:
                            vertiba = gajienavertiba
                            LabakaPos = (gajieni[0], gajieni[1])
                            LabakaisGajiens = (lauks[0], lauks[1])
                        if (gajienavertiba == -math.inf and LabakaPos is None):
                            LabakaPos = (gajieni[0], gajieni[1])
                            LabakaisGajiens = (lauks[0], lauks[1])
                    print('max a ---',LabakaPos,  LabakaisGajiens, vertiba,'    Dzilums==',dzilums)
                    return LabakaPos,  LabakaisGajiens, vertiba
            else:
                vertiba = math.inf
                LabakaPos = None
                LabakaisGajiens = None
                Iespejamie_Gajieni = self.GajienuIegusana(spele)
                for gajieni in Iespejamie_Gajieni:
                    #  print(gajieni)
                    for lauks in gajieni[2]:
                        # print(lauks)
                        self.krasa, self.pretineika = self.pretineika, self.krasa
                        spele.speletajs = self.krasa
                        self.VeiktGajienu(spele, gajieni, lauks)
                        gajienavertiba = self.VertejumsGalda(spele)
                        if gajienavertiba < vertiba:
                            vertiba = gajienavertiba
                            LabakaPos = gajieni
                            LabakaisGajiens = (lauks[0], lauks[1])
                        elif gajienavertiba == vertiba:
                            vertiba = gajienavertiba
                            LabakaPos = (gajieni[0], gajieni[1])
                            LabakaisGajiens = (lauks[0], lauks[1])
                        if (gajienavertiba == -math.inf and LabakaPos is None):
                            LabakaPos = (gajieni[0], gajieni[1])
                            LabakaisGajiens = (lauks[0], lauks[1])
                    print('min a---',LabakaPos,  LabakaisGajiens, vertiba,'    Dzilums==',dzilums)        
                    return LabakaPos,  LabakaisGajiens, vertiba
        else:
            if Speletajs == 'max':
                vertiba = -math.inf
                LabakaPos = None
                LabakaisGajiens = None
                Iespejamie_Gajieni = self.GajienuIegusana(spele)
                for gajieni in Iespejamie_Gajieni:
                    #  print(gajieni)
                    for lauks in gajieni[2]:
                        # print(lauks)
                        self.krasa, self.pretineika = self.pretineika, self.krasa
                        spele.speletajs = self.krasa
                        self.VeiktGajienu(spele, gajieni, lauks)
                        gajienavertiba = self.VertejumsGalda(spele)
                        if spele.beigas():
                            vertiba=math.inf
                        else:
                            h=self.minmax(dzilums-1,spele,'min')
                            if h is not None:
                                _,_, vertiba=h
 
                      #  if vertiba is None:
                      #      continue    
                        self.krasa, self.pretineika = self.pretineika, self.krasa
                        spele.speletajs = self.krasa
                        if gajienavertiba > vertiba:
                            vertiba = gajienavertiba
                            LabakaPos = gajieni
                            LabakaisGajiens = (lauks[0], lauks[1])
                        elif gajienavertiba == vertiba:
                            vertiba = gajienavertiba
                            LabakaPos = (gajieni[0], gajieni[1])
                            LabakaisGajiens = (lauks[0], lauks[1])
                        if (gajienavertiba == -math.inf and LabakaPos is None):
                            LabakaPos = (gajieni[0], gajieni[1])
                            LabakaisGajiens = (lauks[0], lauks[1])
                    print('max b ---',LabakaPos,  LabakaisGajiens, vertiba,'    Dzilums==',dzilums)
                    return LabakaPos,  LabakaisGajiens, vertiba
            else:
                vertiba = math.inf
                LabakaPos = None
                LabakaisGajiens = None
                Iespejamie_Gajieni = self.GajienuIegusana(spele)
                for gajieni in Iespejamie_Gajieni:
                    #  print(gajieni)
                    for lauks in gajieni[2]:
                        # print(lauks)
                        self.krasa, self.pretineika = self.pretineika, self.krasa
                        spele.speletajs = self.krasa
                        self.VeiktGajienu(spele, gajieni, lauks)
                        gajienavertiba = self.VertejumsGalda(spele)
                        if spele.beigas():
                            vertiba=math.inf
                        else:
                            h=self.minmax(dzilums-1,spele,'max')
                            
                       
                            if h is not None:
                                _,_, vertiba=h
     
                            #print(h)
                       # if vertiba is None:
                        #    continue  
                        self.krasa, self.pretineika = self.pretineika, self.krasa
                        spele.speletajs = self.krasa
                        if gajienavertiba < vertiba:
                            vertiba = gajienavertiba
                            LabakaPos = gajieni
                            LabakaisGajiens = (lauks[0], lauks[1])
                        elif gajienavertiba == vertiba:
                            vertiba = gajienavertiba
                            LabakaPos = (gajieni[0], gajieni[1])
                            LabakaisGajiens = (lauks[0], lauks[1])
                        if (gajienavertiba == -math.inf and LabakaPos is None):
                            LabakaPos = (gajieni[0], gajieni[1])
                            LabakaisGajiens = (lauks[0], lauks[1])
                    print('min b---',LabakaPos,  LabakaisGajiens, vertiba,'    Dzilums==',dzilums)
                    return LabakaPos,  LabakaisGajiens, vertiba

    def VeiktGajienu(self, spele, PasPos, BeiguPos):
        #funkcija kas veic gājienu uz speles galda saistiba ar datora gajieniem
        if PasPos is None:
            spele.BeigtGajienu()
            return
        if not spele.lekt:
            laucin = spele.galds.lokacija(BeiguPos[0], BeiguPos[1])
            if laucin.aiznemts != None and laucin.aiznemts.krasa == self.krasa:
                PasPos = BeiguPos
            elif PasPos != None and BeiguPos in spele.galds.atlautieGajieni(PasPos[0], PasPos[1]):
                spele.galds.kustiba(
                    PasPos[0], PasPos[1], BeiguPos[0], BeiguPos[1])
                if BeiguPos not in spele.galds.apkartejie(PasPos[0], PasPos[1]):
                    spele.galds.NonemtKaulinu(PasPos[0]+(BeiguPos[0]-PasPos[0])//2, PasPos[1]+(BeiguPos[1]-PasPos[1])//2)
                    spele.lekt == True
                    PasPos = BeiguPos
                    BeiguPos = spele.galds.atlautieGajieni(
                        PasPos[0], PasPos[1])
                    if BeiguPos != []:
                        self.VeiktGajienu(spele, PasPos, BeiguPos[0])
                        spele.BeigtGajienu()
        if self.spele.lekt:
            if PasPos != None and BeiguPos in spele.galds.atlautieGajieni(PasPos[0], PasPos[1], spele.lekt):
                spele.galds.kustiba(
                    PasPos[0], PasPos[1], BeiguPos[0], BeiguPos[1])
                spele.galds.NonemtKaulinu(
                    PasPos[0]+(BeiguPos[0]-PasPos[0])//2, PasPos[1]+(BeiguPos[1]-PasPos[1])//2)
            if spele.galds.atlautieGajieni(PasPos[0], PasPos[1], spele.lekt) == []:
                spele.BeigtGajienu()
            else:
                PasPos = BeiguPos
                BeiguPos = spele.galds.atlautieGajieni(
                    PasPos[0], PasPos[1], True)
                if BeiguPos == []:
                    self.VeiktGajienu(spele, PasPos, BeiguPos[0])
                spele. BeigtGajienu()
        if spele.lekt != True:
            spele.speletajs = self.pretineika

    def GajienuIegusana(self, spele):
        #funkcija kas izmantota datora gajienu iegušanai
        for x in range(SpelesLaukumaIzmers):
            for y in range(SpelesLaukumaIzmers):
                if spele.galds.atlautieGajieni(x, y, self.spele.lekt) != [] and spele.galds.lokacija(x, y).aiznemts != None and spele.galds.lokacija(x, y).aiznemts .krasa == self.spele.speletajs:
                    yield (x, y, spele.galds.atlautieGajieni(x, y, self.spele.lekt))

    def VisuGajienuIegusana(self, spele): 
        #neizmantota funkcija, bet var aizvietot GajienuIegusana funkciju
        # jo ta tiik atgriez vienu gajienu kamer šī atgriež vairākus uz reiz
        IespGa = []
        for x in range(SpelesLaukumaIzmers):
            for y in range(SpelesLaukumaIzmers):
                if spele.galds.atlautieGajieni(x, y, self.spele.lekt) != [] and spele.galds.lokacija(x, y).aiznemts != None and spele.galds.lokacija(x, y).aiznemts.krasa == self.spele.speletajs:
                    IespGa.append((x, y, spele.galds.atlautieGajieni(x, y, self.spele.lekt)))
        return IespGa

    def KaulinuDaudzums(self, spele): #neizmantota funkcija kaulinu daudzuma apreikinasanai
        Kaul = 0
        for x in range(SpelesLaukumaIzmers):
            for y in range(SpelesLaukumaIzmers):
                aiznemts = spele.galds.lokacija(x, y).aiznemts
                if aiznemts != None:
                    Kaul += 1
        return Kaul

    def VaiVelIrParastie(self, spele): #funkcija izmantota lai noteiktu vai uzgalda ir parastie kaulini
        #tas ir vai nav visas damas
        galds = spele.galds
        for x in range(SpelesLaukumaIzmers):
            for y in range(SpelesLaukumaIzmers):
                aiznemts = galds.lokacija(x, y).aiznemts
                if aiznemts != None and aiznemts.dama == False:
                    return True
        return False

    def KaulVert(self, spele): #neizmantota vertesanas funkcija 
        skaits = 0
        for x in range(SpelesLaukumaIzmers):
            for y in range(SpelesLaukumaIzmers):
                sp = spele.galds.lokacija(x, y)
                if sp.krasa == Melns:
                    if sp.aiznemts != None:

                        if sp.aiznemts.krasa == self.krasa:
                            skaits += sp.aiznemts.vertiba
                        else:
                            skaits -= sp.aiznemts.vertiba
        return skaits

    def VertejumsGalda(self, spele): #funkcu vertibuija kas verte visa galda esošu kauliņ
        Vert = 0
        galds = spele.galds
        if self.krasa == (255, 255, 255):
            for x in range(SpelesLaukumaIzmers):
                for y in range(SpelesLaukumaIzmers):
                    aiznemts = galds.lokacija(x, y).aiznemts
                    if aiznemts != None:
                        if aiznemts.krasa == self.krasa and aiznemts.dama:
                            Vert += 13
                        if aiznemts.krasa != self.krasa and aiznemts.dama:
                            Vert -= 13
                        if aiznemts.krasa == self.krasa and y >= SpelesLaukumaIzmers-3 and aiznemts.dama:    
                            Vert += 5
                        if aiznemts.krasa != self.krasa and y >= SpelesLaukumaIzmers-3 and aiznemts.dama:    
                            Vert -= 5
                        if aiznemts.krasa == self.krasa and y >= SpelesLaukumaIzmers-3 :    
                            Vert += 3
                        if aiznemts.krasa != self.krasa and y >= SpelesLaukumaIzmers-3 :
                            Vert -= 3   
                        if aiznemts.krasa == self.krasa and y < 4:
                            Vert += 5
                        if aiznemts.krasa != self.krasa and y < 4:
                            Vert -= 5
                        if aiznemts.krasa == self.krasa and y >= 4:
                            Vert += 5
                        if aiznemts.krasa != self.krasa and y >= 4:
                            Vert -= 5          
        else:
            for x in range(SpelesLaukumaIzmers):
                for y in range(SpelesLaukumaIzmers):
                    aiznemts = galds.lokacija(x, y).aiznemts
                    if aiznemts != None:
                        if aiznemts.krasa == self.krasa and aiznemts.dama:
                            Vert += 13
                        if aiznemts.krasa != self.krasa and aiznemts.dama:
                            Vert -= 13
                        if aiznemts.krasa == self.krasa and y <= SpelesLaukumaIzmers-3 and aiznemts.dama:    
                            Vert += 5
                        if aiznemts.krasa != self.krasa and y <= SpelesLaukumaIzmers-3 and aiznemts.dama:    
                            Vert -= 5    
                        if aiznemts.krasa == self.krasa and y >= SpelesLaukumaIzmers-3 :    
                            Vert += 3
                        if aiznemts.krasa != self.krasa and y >= SpelesLaukumaIzmers-3 :
                            Vert -= 3       
                        if aiznemts.krasa == self.krasa and y < 4:
                            Vert += 5
                        if aiznemts.krasa != self.krasa and y < 4:
                            Vert -= 5
                        if aiznemts.krasa == self.krasa and y >= 4:
                            Vert += 5
                        if aiznemts.krasa != self.krasa and y >= 4:
                            Vert -= 5
        return Vert



######################################## INICIALIZE MAIN FUNKCIJU #################################################
if __name__ == "__main__":
    main()
    pass
