import pygame
from random import choice
from pygame import Rect, mixer

#Klasa
class Drzave:
    def __init__(self, ime, minX = 0, maxX = 0, minY = 0, maxY = 0):
        self.ime = ime
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY

    def GetIme(self):
        return self.ime

def TrazenaDrzava():
    global prviput
    global ekran
    global ListaDrzava
    global font
    global drz
    global nesto
    

    if nesto == 1 or prviput == 1:
        prviput =0
        #print("Uslo se u if")
        drz = choice(ListaDrzava)
        #ListaDrzava.pop(ListaDrzava.index(drz))
        font=pygame.font.Font('freesansbold.ttf',32)
        DrzavaFont = font.render(drz.GetIme(),True,(255,255,255))
        ekran.blit(DrzavaFont,(285,14))
        nesto = 0
        return drz.ime
    
        #print("uslo se u else")
    DrzavaFont = font.render(drz.GetIme(),True,(255,255,255))
    ekran.blit(DrzavaFont,(285,14))
    return drz.ime

def smjestanje():
    global ListaDrzava
    ListaDrzava.append(island)
    ListaDrzava.append(velikaBritanija)
    ListaDrzava.append(portugal)
    ListaDrzava.append(irska)
    ListaDrzava.append(spanija)
    ListaDrzava.append(francuska)
    ListaDrzava.append(belgija)
    ListaDrzava.append(holandija)
    ListaDrzava.append(luksemburg)
    ListaDrzava.append(svajcarska)
    ListaDrzava.append(italija)
    ListaDrzava.append(njemacka)
    ListaDrzava.append(danska)
    ListaDrzava.append(norveska)
    ListaDrzava.append(svedska)
    ListaDrzava.append(finska)
    ListaDrzava.append(austrija)
    ListaDrzava.append(ceska)
    ListaDrzava.append(slovacka)
    ListaDrzava.append(poljska)
    ListaDrzava.append(litvanija)
    ListaDrzava.append(letonija)
    ListaDrzava.append(estonija)
    ListaDrzava.append(bjelorusija)
    ListaDrzava.append(ukrajina)
    ListaDrzava.append(moldavija)
    ListaDrzava.append(madjarska)
    ListaDrzava.append(rumunija)
    ListaDrzava.append(bugarska)
    ListaDrzava.append(slovenija)
    ListaDrzava.append(hrvatska)
    ListaDrzava.append(bih)
    ListaDrzava.append(srbija)
    ListaDrzava.append(crnagora)
    ListaDrzava.append(albanija)
    ListaDrzava.append(makedonija)
    ListaDrzava.append(grcka)
    ListaDrzava.append(kipar)
    ListaDrzava.append(malta)
    ListaDrzava.append(rusija)

def krajigre(n):
    global fontKraj
    global font
    if n == 0:
        KrajTekst = fontKraj.render("Game over", True, (0,0,0))
        ekran.blit(KrajTekst,(58,260))
    else:
        KrajTekst = fontKraj.render("Game over", True, (255,255,255))
        KrajRestartTekst = font.render("Press R to restart",True,(255,255,255))
        ekran.blit(KrajTekst,(58,260))
        ekran.blit(KrajRestartTekst,(250,400))


#Smjestanje drzava u listu
ListaDrzava = []
island = Drzave("Island", 60, 143, 98, 142)
velikaBritanija = Drzave("Velika Britanija", 160, 235, 245, 362)
portugal = Drzave("Portugal",54,85,474,546)
irska = Drzave("Irska",105,154,296,335)
spanija = Drzave("Spanija", 97, 245, 460, 565)
francuska = Drzave("Francuska", 178,309,381,489)
belgija = Drzave("Belgija", 272,305,360,383)
holandija = Drzave("Holandija", 284,322, 333,366)
luksemburg = Drzave("Luksemburg", 304,313,382,390)
svajcarska = Drzave("Svajcarska", 305,360,418,438)
italija = Drzave("Italija", 334,417,429,573)
njemacka = Drzave("Njemacka", 320,395,310,416)
danska = Drzave("Danska", 341,391,269,310)
norveska = Drzave("Norveska",311,386,148,258)
svedska = Drzave("Svedska",391,464,99,296)
finska = Drzave("Finska",496,550,70,220)
austrija = Drzave("Austrija",360,459,401,433)
ceska = Drzave("Ceska",397,466,369,394)
slovacka = Drzave("Slovacka",470,535,388,402)
poljska = Drzave("Poljska",425,539,311,373)
litvanija = Drzave("Litvanija",501,559,276,302)
letonija = Drzave("Letonija",499,575,250,275)
estonija = Drzave("Estonija",515,559,227,249)
bjelorusija = Drzave("Bjelorusija",548,635,283,334)
ukrajina = Drzave("Ukrajina",550,712,340,384)
moldavija = Drzave("Moldavija",623,645,386,416)
madjarska = Drzave("Madjarska",460,536,412,435)
rumunija = Drzave("Rumunija",538,637,399,453)
bugarska = Drzave("Bugarska",570,643,460,488)
slovenija = Drzave("Slovenija",421,450,434,446)
hrvatska = Drzave("Hrvatska",423,497,436,459)
bih = Drzave("BiH",462,508,452,479)
srbija = Drzave("Srbija",511,556,436,487)
crnagora = Drzave("Crna Gora",502,524,476,492)
albanija = Drzave("Albanija",522,539,488,524)
makedonija = Drzave("Makedonija",540,574,488,505)
grcka = Drzave("Grcka",545,628,515,568)
kipar = Drzave("Kipar",771,796,554,565)
malta = Drzave("Malta",441,452,587,596)
rusija = Drzave("Rusija",607,797,52,310)

smjestanje()


#Inicijalizacija
pygame.init()


#Potrebne promenljive
informacijePozadina =pygame.image.load('help.png')
ekran = pygame.display.set_mode((800, 600))
radi = True
indikator = 0
pozadina = pygame.image.load('pozadina.png').convert()
PlayDugme = pygame.image.load('play.png')
UpitnikDugme = pygame.image.load('question-mark-draw.png')
NazadDugme = pygame.image.load('back-arrow.png')
ZvucnikDugme = pygame.image.load('speaker.png')
RectPlayDugme = PlayDugme.get_rect(center=(400, 300))
RectUpitnikDugme = UpitnikDugme.get_rect(center=(750,550))
RectNazadDugme = NazadDugme.get_rect(center=(50,50))
RectZvucnikDugme = ZvucnikDugme.get_rect(center=(750,50))
zivoti = 3
score = 0
prviput = 1
font=pygame.font.Font('freesansbold.ttf',32)
fontKraj = pygame.font.Font('freesansbold.ttf',128)
drz = choice(ListaDrzava)
nesto = 0
scoreX = 590
muzika = 1

icon = pygame.image.load('map.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("GeoZnanje")

#Muzika
mixer.music.load('Silent_Judgement.wav')
mixer.music.play(-1)
pogodakZvuk =mixer.Sound('click-right.wav')
promasajZvuk = mixer.Sound('click-error.wav')

#Zivoti
zivot1 = pygame.image.load('heart_full_32.png')
zivot2 = pygame.image.load('heart_full_32.png')
zivot3 = pygame.image.load('heart_full_32.png')




#Glavni loop
while radi:
    #Provjera eventova
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            radi = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mX, mY = pygame.mouse.get_pos()
            if event.button == 1:
                #print("radi")
                #print("X koordinata: ", mX)
                #print("Y koordinata: ", mY)
                if (mX>376 and mX<432) and (mY>268 and mY<331) and indikator == 0:
                    pozadina2 = pygame.image.load('Europe_map.png').convert()
                    indikator = 1     #indikator za glavni dio igre
                    mX =0
                    mY = 0
                if (mX>729 and mX<772) and (mY>517 and mY<581) and indikator == 0:
                    indikator = 444
                if (mX>15 and mX<88) and (mY>17 and mY<80) and indikator == 444:
                    indikator = 0
                if (mX>735 and mX<765) and (mY>34 and mY<60) and indikator == 0 and muzika == 1:
                    mixer.music.pause()
                    ZvucnikDugme = pygame.image.load('mute-speaker.png')
                    muzika = 0
                elif (mX>735 and mX<765) and (mY>34 and mY<60) and indikator == 0 and muzika == 0:
                    mixer.music.play()
                    ZvucnikDugme = pygame.image.load('speaker.png')
                    muzika = 1
        if event.type == pygame.KEYDOWN and indikator==888:
            if event.key==pygame.K_r:
                indikator = 1
                score = 0
                zivoti = 3
                zivot2 = pygame.image.load('heart_full_32.png')
                zivot3 = pygame.image.load('heart_full_32.png')



    #crtanje na ekranu
    ekran.fill((0, 0, 0))
    if indikator == 0:
        ekran.blit(pozadina, (0, 0))
        ekran.blit(PlayDugme, RectPlayDugme)
        ekran.blit(UpitnikDugme, RectUpitnikDugme)
        ekran.blit(ZvucnikDugme, RectZvucnikDugme)
    elif indikator == 1:
        ekran.blit(pozadina2, (0,50))
        trazenoime= TrazenaDrzava()
        TekstScore = font.render("SCORE: " + str(score), True, (255,255,255))
        ekran.blit(TekstScore,(scoreX,14))
        ekran.blit(zivot1,(10,14))
        ekran.blit(zivot2,(42,14))
        ekran.blit(zivot3,(74,14))
        #print(trazenoime)
        for i in ListaDrzava:
            if (mX>i.minX and mX<i.maxX) and (mY>i.minY and mY<i.maxY):
                if i.ime == trazenoime:
                    #print(i.ime)
                    mX = 0
                    mY = 0
                    pogodakZvuk.play()
                    score +=100
                    if score >= 10000:
                        scoreX = 575
                    #print(score)
                    nesto = 1
                    break
                else:
                    zivoti -= 1
                    promasajZvuk.play()
                    #print(zivoti)
                    mX = 0
                    mY = 0
                    if zivoti == 2:
                        zivot3 = pygame.image.load('heart_lost_32.png')
                    if zivoti == 1:
                        zivot2 = pygame.image.load('heart_lost_32.png')
                    break
            if zivoti <= 0:
                krajigre(0)
                indikator = 888
    elif indikator == 888:
        krajigre(1)
    else:
        ekran.blit(informacijePozadina,(0,0))
        ekran.blit(NazadDugme,RectNazadDugme)


    pygame.display.update()
