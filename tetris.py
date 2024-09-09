import pygame, sys, random, time, copy
from pygame.locals import *
pg=pygame
pd=pg.display
pg.init()
rozmiar=600
BIALY = (255,255,255)
CZARNY = (0,0,0)
NIEBIESKI = (0,0,255)   
CZERWONY = (220,0,0)
ZIELONY = (0,200,0)
FIOLET = (147,112,219)
ZOLTY = (255,255,0)
POM = (255,165,0)
mapa = pd.set_mode((rozmiar, rozmiar))
czcionka = pg.font.SysFont("Comic Sans MS", 18)
dczcionka = pg.font.SysFont("Comic Sans MS", 100)
sczcionka = pg.font.SysFont("Comic Sans MS", 30)

def text(text, font, color = CZARNY):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

    
def przycisk(msg, x, y, width, height, color, action = None):
    width_half = width / 2
    height_half = height / 2
    mouse = pg.mouse.get_pos() 
    click = pg.mouse.get_pressed()
    pg.draw.rect(mapa, color, (x, y, width, height))
    if (x < mouse[0] < (x + width)) and (y < mouse[1] < (y + height)):
        if (click[0] == 1) and (action != None):
            action()
    text_surf, text_rect = text(msg, czcionka)
    text_rect.center = (x + width_half, y + height_half)
    mapa.blit(text_surf, text_rect)

    
def wyj():
    sys.exit(0)

    
def wyniki():
    while True:
        o=pg.image.load("file.jpg")
        mapa.blit(o,(0,0))
        for e in pg.event.get():
            if e.type==pg.QUIT:
                wyj()
            if e.type==KEYDOWN:
                if e.key==K_o:
                    pg.mixer.music.pause()
                if e.key==K_i:        
                    pg.mixer.music.unpause()
        przycisk("",180,240,250,250,CZARNY)
        przycisk("powrot", 400, 500, 200, 100, CZERWONY, menu)
        lista=[]
        plik = open("plik.txt", "r").read()
        lines = plik.split("\n")
        for line in lines:
            if line != "":
                lista.append(int(line))
        lista.sort()
        lista.reverse()
        b=300
        text_surf, text_rect = text("Najlepsze wyniki",sczcionka,BIALY)
        text_rect.center = (300,b-40)
        mapa.blit(text_surf, text_rect)
        for g in range (10):
            text_surf, text_rect = text(str(g+1)+"."+ str(lista[g]) +" pkt",czcionka,BIALY)
            text_rect.center = (300,b)
            mapa.blit(text_surf, text_rect)
            b=b+20
        pd.update()


def klocki():
    while True:
        o=pg.image.load("klocki.jpg")
        mapa.blit(o,(0,0))
        for e in pg.event.get():
            if e.type==pg.QUIT:
                wyj()
            if e.type==KEYDOWN:
                if e.key==K_o:
                    pg.mixer.music.pause()
                if e.key==K_i:        
                    pg.mixer.music.unpause()
        przycisk("nastepne",0,500,100,100,FIOLET,klocki1)
        przycisk("menu",500,500,100,100,CZERWONY,menu)
        pd.update()


def klocki1():
    o=pg.image.load("klocki1.jpg")
    while True:
        mapa.blit(o,(0,0))
        for e in pg.event.get():
            if e.type==pg.QUIT:
                wyj()
            if e.type==KEYDOWN:
                if e.key==K_o:
                    pg.mixer.music.pause()
                if e.key==K_i:        
                    pg.mixer.music.unpause()
        przycisk("poprzednie",0,400,100,100,FIOLET,klocki)
        przycisk("menu",500,500,100,100,CZERWONY,menu)
        pd.update()


def pauza():    
    x=1
    while x:
        text_surf, text_rect = text("Pauza", dczcionka,NIEBIESKI)
        text_rect.center = (rozmiar / 2), ((rozmiar-300) / 2)
        mapa.blit(text_surf, text_rect)
        przycisk("Reset", 400, 350, 200, 100, ZIELONY)
        przycisk("Menu", 400, 450, 200, 100, CZERWONY)
        pd.update()
        for e in pg.event.get():
            przycisk("Reset", 400, 350, 200, 100, ZIELONY,gra)
            przycisk("Menu", 400, 450, 200, 100, CZERWONY, menu)
            if e.type==pg.QUIT:
                wyj()
            if e.type==KEYDOWN:
                if e.key==K_o:
                    pg.mixer.music.pause()
                if e.key==K_i:        
                    pg.mixer.music.unpause()
                if e.key==K_p:
                    x=0


def main():
    pg.mixer.music.load("Epic Sax Guy.mp3")
    pg.mixer.music.play(-1)
    pd.set_caption("Tetris")
    menu()
    
    
def menu():
    obraz=pg.image.load("file.jpg")
    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit(0)
            if e.type==KEYDOWN:
                if e.key==K_o:
                    pg.mixer.music.pause()
                if e.key==K_i:        
                    pg.mixer.music.unpause()
        mapa.blit(obraz,(0,0))
        text_surf, text_rect = text("Tetris", dczcionka,NIEBIESKI)
        text_rect.center = (rozmiar / 2), ((rozmiar-300) / 2)
        mapa.blit(text_surf, text_rect)
        przycisk("Graj", 200, 200, 200, 100, ZIELONY, gra)
        przycisk("Wyniki", 200, 300, 200, 100, ZOLTY, wyniki)
        przycisk("klocki", 200, 400, 200, 100,POM , klocki)
        przycisk("Wyjscie", 200, 500, 200, 100, CZERWONY, wyj)
        pd.update()


def gra():
    cdc=copy.deepcopy
    pc=[[[1,1],[1,1]],[[1,0],[1,0],[1,1]],[[0,1],[0,1],[1,1]],[[1],[1],[1],[1]],[[0,1,1],[1,1,0]],[[1,1,0],[0,1,1]],[[1,1,1],[0,1,0]],[[1]],[[1,0,0],[1,1,1],[1,0,0]],[[1,0],[1,1],[1,1],[1,0]]]
    kolory=[(0,0,0),(100,100,100),(10,100,225),(0,150,220),(0,220,150),(60,200,10),(180,210,5),(210,180,10),(100,200,170),(30,30,30),(255,0,0),(255,165,0)]
    q=10
    sk=pd.get_surface()
    f=[[1]+[0 for x in range(q)]+[1] for x in range(23)]+[[1 for x in range(q+2)]]
    of=cdc(f)
    s=21
    kratka=Rect((100,0,s,s))
    b=-1
    p=[]
    lc=[-9,0]
    t=0
    bt=60
    pg.key.set_repeat(200,100)
    rh=0
    gv=-1
    _=0
    h=6
    nb=random.randint(0,h)
    
    while 1:
        if _ >=100:
            h=7
            bt=45
            if _ >=200:
                h=8
                bt=30
                if _ >=500:
                    h=9
                    bt=20
                    
        sk.fill((0,0,0))
        text_surf, text_rect = text("Wynik: " + str(_),czcionka,BIALY)
        text_rect.center = (500,250)
        sk.blit(text_surf, text_rect)
        text_surf, text_rect = text("p-pauza",czcionka,BIALY)
        text_rect.center = (500,270)
        sk.blit(text_surf, text_rect)
        text_surf, text_rect = text("o-wylacz muzyke",czcionka,BIALY)
        text_rect.center = (500,290)
        sk.blit(text_surf, text_rect)
        text_surf, text_rect = text("i-wlacz muzyke",czcionka,BIALY)
        text_rect.center = (500,310)
        sk.blit(text_surf, text_rect)
        o=pg.image.load("reklama.jpg")
        sk.blit(o,(130,520))
        
        if gv>-1:
            b=10
            rh=0
            if not t%5:
                gv-=1
                f[9-gv]=[1]*10
                f[10+gv]=[1]*10
                t=1
            if gv==0:
                gv=99
                
        if b<-1:
            b+=1
        if b==-1:
            b=nb
            bk=nb
            p=pc[bk]
            nb=random.randint(0,h)
            lc=[(q-4)-int(len(p)/2),0]
            
        if not t%bt or rh:
            op=[p[:],lc[:]]
            lc[1] +=1
            
        if b < 0:
            continue
        rx=0
        c=0
        
        for l in p:
            r=0
            for k in l:
                while c+lc[0]<1:
                    lc[0]+=1
                while c+lc[0]>q:
                    lc[0]-=1
                if f[r + lc[1]][c + lc[0]] and k:
                    if lc[1]==0:
                        gv=1
                    rx=1
                r+=1
            c+=1
            
        if rx :
            p,lc=op
            c=0
            for l in p:
                r=0
                for k in l:
                    if k:
                        f[r+lc[1]][c+lc[0]]=b+2
                    r+=1
                c+=1
            b=-20
            t=1
            rx=0
            rh=0
            p=[]
        
        if rh:
            continue
        
        for r in f[:-1]:
            if not r.count(0):
                wr=r
                f.remove(wr)
                f=[[1]+[0 for x in range(q)]+[1]]+f
                if gv==-1:
                    _+=10
                    
        if gv>-1:
            f=cdc(of)
        
        c=0
        for l in f:
            r=0
            for k in l:
                try:
                    if r>=lc[0] and c>=lc[1] and p[r-lc[0]][c-lc[1]]:
                        k=b+2
                except:
                    pass
                sk.fill(kolory[k],kratka.move(r*s,c*s).inflate(-2,-2))
                r+=1
            c+=1
            
        if gv==99:
            text_surf, text_rect = text("Game over",czcionka,BIALY)
            text_rect.center = (220,250)
            sk.blit(text_surf, text_rect)
            plik = open("plik.txt", "a")
            plik.write(str(_)+"\n")
            plik.close()
            pd.flip()
            time.sleep(0.5)
            menu()
                
        for x in range(10):
            if x==nb:
                o=pg.image.load(str(x)+".jpg")
                mapa.blit(o,(450,80))
                
        text_surf, text_rect = text("nastepny klocek:",czcionka,BIALY)
        text_rect.center = (500,50)
        sk.blit(text_surf, text_rect)
        przycisk("Reset", 400, 350, 200, 100, ZIELONY)
        przycisk("Menu", 400, 450, 200, 100, CZERWONY, menu)
        pd.flip()
        t+=1
        time.sleep(0.01)
        
        if gv>=0:
            continue
        
        for e in pg.event.get():
            przycisk("Reset", 450, 350, 200, 100, ZIELONY,gra)
            if e.type== pg.QUIT:
                sys.exit(0)
            if e.type==KEYDOWN:
                if e.key==K_p:
                    pauza()
                if e.key==K_o:
                    pg.mixer.music.pause()
                if e.key==K_i:        
                    pg.mixer.music.unpause()
                if e.key==K_LEFT:
                    op=[p[:],lc[:]]
                    lc[0]-=1
                if e.key==K_RIGHT:
                    op=[p[:],lc[:]]
                    lc[0]+=1
                if e.key==K_DOWN:
                    op=[p[:],lc[:]]
                    lc[1]+=1;t=1
                if e.key==K_UP and p:
                    op=[p[:],lc[:]]
                    p=[[p[x][-y-1] for x in range(len(p))] for y in range(len(p[0]))]
                if e.key==K_SPACE:
                    rh=1
main()