import pygame
import os
import math
import random
from random import randint
import csv
pygame.font.init()

WIDTH, HEIGHT = 650, 650
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Titan")

HERO_HIT = pygame.USEREVENT + 1
VILL_HIT = pygame.USEREVENT + 2
JSHI_HIT = pygame.USEREVENT + 3
JSHI_HITH = pygame.USEREVENT + 4
P1S = pygame.USEREVENT + 5
P2S = pygame.USEREVENT + 6
P3S = pygame.USEREVENT + 7
RESETT = pygame.USEREVENT + 8
DRESETT = pygame.USEREVENT + 9
RESTARTT = pygame.USEREVENT + 10
RESUMEE = pygame.USEREVENT + 11
MENUU = pygame.USEREVENT + 12

PFONT = pygame.font.SysFont('fixedsys', 25)
TFONT = pygame.font.SysFont('castellar', 60)
FFONT = pygame.font.SysFont('castellar', 30)
SFONT = pygame.font.SysFont('castellar', 20)

bglas = pygame.image.load(os.path.join('Assets', 'turrLas.png'))
bplas = pygame.image.load(os.path.join('Assets', 'plas.png'))
bolas = pygame.image.load(os.path.join('Assets', 'olas.png'))

h1 = pygame.image.load(os.path.join('Assets', 'heroshipDr.png'))
bgi = pygame.image.load(os.path.join('Assets', 'Sbgr2.jpg'))
prii = pygame.image.load(os.path.join('Assets', 'shipRO.png'))
turrB = pygame.image.load(os.path.join('Assets', 'turbas.png'))
turr = pygame.image.load(os.path.join('Assets', 'turretRa.png'))
shieF = pygame.image.load(os.path.join('Assets', 'shieF.png'))
shieR = pygame.image.load(os.path.join('Assets', 'shieR.png'))
drimg = pygame.image.load(os.path.join('Assets', 'ufoul.png'))
MAXBU = 20
colorre = (100,100,100)
colorret = (100,100,100)
p1b = (100,100,100)
p2b = (100,100,100)
p3b = (100,100,100)
coly = (100,100,100)
coln = (100,100,100)
comm = 0


def draw_window(hero, angl, bullets, vBullets, ang, pri, Tbase, vang, jshie, jang, droids, state, playe, hs1, hs2, hs3, score, health, ssta, comm):
    
    #title playerSelect
    if state == 0:
        WIN.fill((0,0,0))
        
        if mouseU(260+75, 290+15, 80, 15) == True:
            p1b = (0,255,0)
        else:
            p1b = (100,100,100)


        if mouseU(260+75, 340+15, 80, 15) == True:
            p2b = (0,255,0)
        else:
            p2b = (100,100,100)


        if mouseU(260+75, 390+15, 80, 15) == True:
            p3b = (0,255,0)
        else:
            p3b = (100,100,100)


        topi = TFONT.render("Titan", 1, (0,255,0))
        pl1 = FFONT.render("Player_1", 1, p1b)
        pl2 = FFONT.render("Player_2", 1, p2b)
        pl3 = FFONT.render("Player_3", 1, p3b)
        resu = FFONT.render("select player to continue", 1, (0,255,0))
        WIN.blit(topi, (230,200))
        WIN.blit(pl1, (260,290))
        WIN.blit(pl2, (260,340))
        WIN.blit(pl3, (260,390))
        WIN.blit(resu, (100,450))

        if pygame.mouse.get_pressed()[0] and comm == 20:
            if mouseU(260+75, 290+15, 80, 15) == True:             
               pygame.event.post(pygame.event.Event(P1S))

            if mouseU(260+75, 340+15, 80, 15) == True:
                pygame.event.post(pygame.event.Event(P2S))

            if mouseU(260+75, 390+15, 80, 15) == True:
                pygame.event.post(pygame.event.Event(P3S))

    #highscore reset
    if state == 1:
        
        WIN.fill((0,0,0))
        
        if playe == 2 and hs2!=0:

            if mouseU(175+75, 390+15, 30, 15) == True:
                p1b = (0,255,0)
            else:
                p1b = (100,100,100)


            if mouseU(333+75, 390+15, 27, 15) == True:
                p2b = (0,255,0)
            else:
                p2b = (100,100,100)


            sen1 = FFONT.render("would you like to reset", 1, (0,255,0))
            sen2 = FFONT.render("the highScore of the player", 1, (0,255,0))
            yess = FFONT.render("YES", 1, p1b)
            noo = FFONT.render("NO", 1, p2b)

            WIN.blit(sen1, (100,230))
            WIN.blit(sen2, (100,290))
            WIN.blit(yess, (220,390))
            WIN.blit(noo, (380,390))

            if pygame.mouse.get_pressed()[0] and comm == 20:
                if mouseU(175+75, 390+15, 30, 15) == True:            
                   pygame.event.post(pygame.event.Event(RESETT))

                if mouseU(333+75, 390+15, 27, 15) == True:
                    pygame.event.post(pygame.event.Event(DRESETT))


        elif playe == 2 and hs2 == 0:
            pygame.event.post(pygame.event.Event(DRESETT))

        if playe == 3 and hs3!=0:

            if mouseU(175+75, 390+15, 30, 15) == True:
                p1b = (0,255,0)
            else:
                p1b = (100,100,100)


            if mouseU(333+75, 390+15, 27, 15) == True:
                p2b = (0,255,0)
            else:
                p2b = (100,100,100)


            sen1 = FFONT.render("would you like to reset", 1, (0,255,0))
            sen2 = FFONT.render("the highScore of the player", 1, (0,255,0))
            yess = FFONT.render("YES", 1, p1b)
            noo = FFONT.render("NO", 1, p2b)

            WIN.blit(sen1, (100,230))
            WIN.blit(sen2, (100,290))
            WIN.blit(yess, (220,390))
            WIN.blit(noo, (380,390))

            if pygame.mouse.get_pressed()[0]:
                if mouseU(175+75, 390+15, 30, 15) == True:            
                   pygame.event.post(pygame.event.Event(RESETT))

                if mouseU(333+75, 390+15, 27, 15) == True:
                    pygame.event.post(pygame.event.Event(DRESETT))


        elif playe == 3 and hs3 == 0:
            pygame.event.post(pygame.event.Event(DRESETT))

        if playe == 1 and hs1!=0:

            if mouseU(175+75, 390+15, 30, 15) == True:
                p1b = (0,255,0)
            else:
                p1b = (100,100,100)


            if mouseU(333+75, 390+15, 27, 15) == True:
                p2b = (0,255,0)
            else:
                p2b = (100,100,100)


            sen1 = FFONT.render("would you like to reset", 1, (0,255,0))
            sen2 = FFONT.render("the highScore of the player", 1, (0,255,0))
            yess = FFONT.render("YES", 1, p1b)
            noo = FFONT.render("NO", 1, p2b)

            WIN.blit(sen1, (100,230))
            WIN.blit(sen2, (100,290))
            WIN.blit(yess, (220,390))
            WIN.blit(noo, (380,390))

            if pygame.mouse.get_pressed()[0]:
                if mouseU(175+75, 390+15, 30, 15) == True:            
                   pygame.event.post(pygame.event.Event(RESETT))

                if mouseU(333+75, 390+15, 27, 15) == True:
                    pygame.event.post(pygame.event.Event(DRESETT))


        elif playe == 1 and hs1 == 0:
            pygame.event.post(pygame.event.Event(DRESETT))

    #story controls
    if state == 11:
        WIN.fill((0,0,0))
        sen1 = SFONT.render("YOU are the last standing pilot", 1, (0,255,0))
        sen2 = SFONT.render("of Titan, the one to defend its", 1, (0,255,0))
        sen3 = SFONT.render("honor.", 1, (0,255,0))
        sen4 = SFONT.render("you must hold of the alien UFOs", 1, (0,255,0))
        sen5 = SFONT.render("as long as you can to protect", 1, (0,255,0))
        sen6 = SFONT.render("the technology of Titan's ", 1, (0,255,0))
        sen7 = SFONT.render("light-speed warp jet.", 1, (0,255,0))
        sen8 = SFONT.render("move with w,a,s,d and spaceBar", 1, (0,255,0))
        sen9 = SFONT.render("to shoot", 1, (0,255,0))
        sen10 = SFONT.render("Press 'p' to play", 1, (0,255,0))

        WIN.blit(sen1, (10,10))
        WIN.blit(sen2, (10,40))
        WIN.blit(sen3, (10,70))
        WIN.blit(sen4, (10,70+30))
        WIN.blit(sen5, (10,70+60))
        WIN.blit(sen6, (10,70+90))
        WIN.blit(sen7, (10,70+120))
        WIN.blit(sen8, (10,70+180))
        WIN.blit(sen9, (10,70+210))
        WIN.blit(sen10, (10,70+290))

        h1r = pygame.transform.rotate(h1, angl)
        h1r_rect = h1r.get_rect(center = (325, 325))
        WIN.blit(h1r, h1r_rect)

    #ingame menu
    if state == 22:
        WIN.fill((0,0,0))

        if mouseU(270+65, 290+15, 60, 15):
            colorre = (0,255,0)
        else:
            colorre = (100,100,100)

        if mouseU(270+65, 340+15, 70, 15):
            colorret = (0,255,0)
        else:
            colorret = (100,100,100)

        if mouseU(270+60, 390+15, 50, 15):
            colormen = (0,255,0)
        else:
            colormen = (100,100,100)

        topi = TFONT.render("Titan", 1, (0,255,0))
        resu = FFONT.render("resume", 1, colorre)
        resta = FFONT.render("restart", 1, colorret)
        menua = FFONT.render("menu", 1, colormen)
        WIN.blit(topi, (230,200))
        WIN.blit(resu, (270,290))
        WIN.blit(resta, (267,340))
        WIN.blit(menua, (280,390))

        if pygame.mouse.get_pressed()[0] and comm==20:
            if mouseU(270+65, 290+15, 60, 15) == True:            
               pygame.event.post(pygame.event.Event(RESUMEE))

            if mouseU(270+65, 340+15, 70, 15) == True:
                pygame.event.post(pygame.event.Event(RESTARTT))
            
            if mouseU(270+60, 390+15, 50, 15) == True:
                pygame.event.post(pygame.event.Event(MENUU))

    #game loop
    if state == 3:
        WIN.fill((0,0,0))
        anggg = 0

        h1r = pygame.transform.rotate(h1, angl)
        h1r_rect = h1r.get_rect(center = (hero.x, hero.y))

        priir = pygame.transform.rotate(prii, -45)
        priir_rect = priir.get_rect(center = (pri.x,pri.y))

        turb = pygame.transform.rotate(turrB, 0)
        turb_rect = turb.get_rect(center = (Tbase.x,Tbase.y))
        uupp = (hero.x)-(Tbase.x)
        ddoww = (hero.y)-(Tbase.y)
        if uupp>0 and ddoww==0:
            anggg = -90
        elif uupp<0 and ddoww==0:
            anggg = 90
        elif uupp==0 and ddoww<0:
            anggg = 0
        elif uupp==0 and ddoww>0:
            anggg = 180
        elif (uupp<0 and ddoww<0) or (uupp>0 and ddoww<0):
            anggg = math.degrees(math.atan(uupp/ddoww))
        elif (uupp<0 and ddoww>0) or (uupp>0 and ddoww>0):
            anggg = math.degrees(math.atan(uupp/ddoww))+180
        elif uupp == 0 and ddoww == 0:
            anggg = anggg

        tur = pygame.transform.rotate(turr, anggg)
        tur_rect = tur.get_rect(center = (Tbase.x,Tbase.y))


        bgir = pygame.transform.scale(bgi,(650,650))
        WIN.blit(bgir, (0,0))
        WIN.blit(h1r, h1r_rect)
        WIN.blit(priir, priir_rect)
        
        #pygame.draw.rect(WIN, (0,255,255), Tbase)
        #pygame.draw.rect(WIN, (255,255,255), jsD)
        #pygame.draw.rect(WIN, (255,255,0), heroD)

        for i,elements in enumerate(bullets):
            bullet = bullets[i]
            bu = pygame.transform.rotate(bolas, ang[i])
            bu_rect = bu.get_rect(center = (bullet.x, bullet.y))
            WIN.blit(bu, bu_rect)

        for i,elements in enumerate(droids):
            droid = droids[i]
            ufo = pygame.transform.rotate(drimg, -1*jang)
            ufo_rect = ufo.get_rect(center = (droid.x, droid.y))
            WIN.blit(ufo, ufo_rect)


        for i,elements in enumerate(vBullets):
            vbullet = vBullets[i]
            vbu = pygame.transform.rotate(bglas, vang[i])
            vbu_rect = vbu.get_rect(center = (vbullet.x, vbullet.y))
            WIN.blit(vbu, vbu_rect)

        WIN.blit(turb, turb_rect)
        WIN.blit(tur, tur_rect)
        
        jshiel = pygame.transform.rotate(shieR, jang)
        jshiel_rect = jshiel.get_rect(center = (jshie.x,jshie.y))
        WIN.blit(jshiel, jshiel_rect)

        scoreT = PFONT.render("score: "+str(score), 1, (0,255,0))
        healthT = PFONT.render("health: "+str(health), 1, (0,255,0))
        if playe == 1:
            highscoreT = PFONT.render("High Score: "+str(hs1), 1, (0,255,0))
        if playe == 2:
            highscoreT = PFONT.render("High Score: "+str(hs2), 1, (0,255,0))
        if playe == 3:
            highscoreT = PFONT.render("High Score: "+str(hs3), 1, (0,255,0))
        sstaT = PFONT.render("Sheild Stability: "+str(ssta), 1, (0,255,0))
        WIN.blit(scoreT, (40,520))
        WIN.blit(healthT, (40,540))
        WIN.blit(highscoreT, (40,560))
        WIN.blit(sstaT, (40,580))
    
    if state == 111:
        WIN.fill((0,0,0))
        
        if mouseU(225+100, 320+15, 100, 15):
            p1b = (0,255,0)
        else:
            p1b = (100,100,100)

        if mouseU(270+50, 390+15, 50, 15):
            p2b = (0,255,0)
        else:
            p2b = (100,100,100)

        goT = TFONT.render("GAME OVER", 1, (0,255,0))
        scoreT = PFONT.render("score: "+str(score), 1, (0,255,0))
        if playe == 1:
            highscoreT = PFONT.render("High Score: "+str(hs1), 1, (0,255,0))
        if playe == 2:
            highscoreT = PFONT.render("High Score: "+str(hs2), 1, (0,255,0))
        if playe == 3:
            highscoreT = PFONT.render("High Score: "+str(hs3), 1, (0,255,0))
        plaaT = FFONT.render("play again", 1, p1b)
        menuT = FFONT.render("Menu", 1, p2b)
        WIN.blit(goT, (130,100))
        WIN.blit(scoreT, (300,180))
        WIN.blit(highscoreT, (270,210))
        WIN.blit(plaaT, (225,320))
        WIN.blit(menuT, (270,390))

        if pygame.mouse.get_pressed()[0] and comm==20:
            if mouseU(225+100, 320+15, 100, 15)==True:            
               pygame.event.post(pygame.event.Event(RESTARTT))

            if mouseU(270+50, 390+15, 50, 15) == True:
                pygame.event.post(pygame.event.Event(MENUU))

    #gameOver menu
    pygame.display.update()



def mouseU(xx, yy, amtx, amty):
    mousee = pygame.mouse.get_pos()
    if mousee[0]>xx-amtx and mousee[0]<xx+amtx and mousee[1]>yy-amty and mousee[1]<yy+amty:
        return True
    else:
        return False

def interB(o1, o2, amt):
    if o1.x>o2.x-amt and o1.x<o2.x+amt and o1.y>o2.y-amt and o1.y<o2.y+amt:
        return True
    else:
        return False

def colStop(o1, o2, mar):

    if o1.y<(o2.y+mar) and o1.y>(o2.y-mar):
        if o1.x>o2.x-mar-1 and o1.x<o2.x:
            o1.x = o2.x-mar
        if o1.x<o2.x+mar+1 and o1.x>o2.x:
            o1.x = o2.x+mar

    if o1.x<(o2.x+mar) and o1.x>(o2.x-mar):
        if o1.y>o2.y-mar and o1.y<o2.y:
            o1.y = o2.y-mar
        if o1.y<o2.y+mar and o1.y>o2.y:
            o1.y = o2.y+mar

def fireCheckBu(vBullets, bullets, droids, hero, ang, vang, heroD, jsD, state):
    
    for i,element in enumerate(droids):
        droid = droids[i]
        uup = (droid.x)-(WIDTH/2)
        ddow = (droid.y)-(HEIGHT/2)
        if uup>0 and ddow==0:
            angg = -90
        elif uup<0 and ddow==0:
            angg = 90
        elif uup==0 and ddow<0:
            angg = 0
        elif uup==0 and ddow>0:
            angg = 180
        elif (uup<0 and ddow<0) or (uup>0 and ddow<0):
            angg = math.degrees(math.atan(uup/ddow))
        elif (uup<0 and ddow>0) or (uup>0 and ddow>0):
            angg = math.degrees(math.atan(uup/ddow))+180
        elif uup == 0 and ddow == 0:
            angg = angg
        if state == 3:
            droid.x+=1*math.sin(math.radians(angg))
            droid.y+=1*math.cos(math.radians(angg))
    
    
    for i,element in enumerate(bullets):
        bullet = bullets[i]
        if state == 3:
            bullet.x-=20*math.sin(math.radians(ang[i]))
            bullet.y-=20*math.cos(math.radians(ang[i]))
        if len(bullets)>10:
            bullets.pop(i)
            for j in range(10):
                ang[j] = ang[j+1]

        for droid in droids:
            if interB(bullet, droid, 25) == True:
                pygame.event.post(pygame.event.Event(VILL_HIT))
                bullets.remove(bullet)
                droids.remove(droid)
        
        if jsD.colliderect(bullet):
            pygame.event.post(pygame.event.Event(JSHI_HITH))
            bullets.remove(bullet)
                

    for i,element in enumerate(vBullets):
        vbullet = vBullets[i]
        if state == 3:
            vbullet.x-=20*math.sin(math.radians(vang[i]))
            vbullet.y-=20*math.cos(math.radians(vang[i]))
        if len(vBullets)>10:
            vBullets.pop(i)
            for j in range(10):
                vang[j] = vang[j+1]

        if heroD.colliderect(vbullet):
            pygame.event.post(pygame.event.Event(HERO_HIT))
            vBullets.remove(vbullet)

        if jsD.colliderect(vbullet):
            pygame.event.post(pygame.event.Event(JSHI_HIT))
            vBullets.remove(vbullet)


def main():

    bg = pygame.Rect(0,0,700,700)
    hero = pygame.Rect(100,100, 50, 50)
    heroD = pygame.Rect(hero.x+25, hero.y+25, 30,30)
    Tbase = pygame.Rect(70,70,80,80)
    jshie = pygame.Rect(WIDTH/2, HEIGHT/2,70,70)
    jsD = pygame.Rect(jshie.x-35, jshie.y-35,70,70)
    jang = 0
    listt = [(325,30),(325, 620),(30,620),(620,30), (620,620), (30,325)]

    anglee = 0
    angg = 0
    timr = 0
    dtimr = 0
    iik=0
    iij=0
    state = 0
    playe = 2
    score=0
    hs1=0
    hs2=0
    hs3 = 0
    health=10
    ssta = 10
    comm = 0
    intes=[]

    f = open("hsdat.csv", "r")
    fread = csv.reader(f)
    for inte in fread:
        intes.append(inte)
    f.close()

    hs1 = intes[0]
    hs1 = int(hs1[0])
    hs2 = intes[2]
    hs2 = int(hs2[0])
    hs3 = intes[4]
    hs3 = int(hs3[0])
    print(hs1)
    print(hs2)
    print(hs3)

    bullets = []
    vBullets = []
    droids = []
    ang = [1,1,1,1,1,1,1,1,1,1,1]
    vang = [1,1,1,1,1,1,1,1,1,1,1]
    
    pri=pygame.Rect(HEIGHT/2, WIDTH/2, 30,30)
    
    clock = pygame.time.Clock()
    run = True
    while run: 
        #if state == 0:
         #   draw_menu()
          #  kePre = pygame.key.get_pressed()
           # if kePre[pygame.K_p]:
            #    state = 1
        #elif state == 1:
        clock.tick(60)

        if comm<20:
            comm+=1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(hero.x, hero.y, 20,20)
                    ang[iij] = anglee
                    bullets.append(bullet)
                    if iij<10:
                        iij+=1
            
            if event.type == HERO_HIT:
                iik-=1
                if health > 0:
                    health-=1
                if health == 0:
                    comm = 0
                    state = 111

            if event.type == VILL_HIT:
                iij-=1
                score+=1
                if playe == 1:
                    if score>hs1:
                        hs1 = score
                if playe == 2:
                    if score>hs2:
                        hs2 = score
                if playe == 3:
                    if score>hs3:
                        hs3 = score

            if event.type == JSHI_HIT:
                iik-=1

            if event.type == JSHI_HITH:
                iij-=1

            if event.type == P1S:
                playe = 1
                comm = 0
                state = 1
            if event.type == P2S:
                playe = 2
                comm = 0
                state = 1
            if event.type == P3S:
                playe = 3
                comm = 0
                state = 1

            if event.type == RESETT:
                if playe ==1:
                    hs1 = 0
                    comm = 0
                    state = 11
                if playe ==2:
                    hs2 = 0
                    comm = 0
                    state = 11
                if playe ==3:
                    hs3 = 0
                    comm = 0
                    state = 11

            if event.type == MENUU:
                health = 10
                ssta = 10
                timr = 0
                dtimr = 0
                for droid in droids:
                    droids.remove(droid)
                score = 0
                comm = 0
                state = 0

            if event.type == RESUMEE:
                comm = 0
                state = 3
                

            if event.type == RESTARTT:
                health = 10
                ssta = 10
                timr = 0
                dtimr = 0
                for droid in droids:
                    droids.remove(droid)
                score = 0
                comm = 0
                state = 3

            if event.type == DRESETT:
                comm = 0
                state = 11
        
        if state == 3:
            timr+=1
        #canon fire..
        if timr == 240 and state == 3:
            vbullet = pygame.Rect(Tbase.x, Tbase.y, 20,20)
            uup = (hero.x)-(Tbase.x)
            ddow = (hero.y)-(Tbase.y)
            if uup>0 and ddow==0:
                angg = -90
            elif uup<0 and ddow==0:
                angg = 90
            elif uup==0 and ddow<0:
                angg = 0
            elif uup==0 and ddow>0:
                angg = 180
            elif (uup<0 and ddow<0) or (uup>0 and ddow<0):
                angg = math.degrees(math.atan(uup/ddow))
            elif (uup<0 and ddow>0) or (uup>0 and ddow>0):
                angg = math.degrees(math.atan(uup/ddow))+180
            elif uup == 0 and ddow == 0:
                angg = angg
            vang[iik] = angg
            vBullets.append(vbullet)
            if iik<10:
                iik+=1
        if timr>240 and state == 3:
            timr=0
        

        if state == 3:
            dtimr+=1
        if dtimr==120:
            if len(droids)<10 and state == 3:
                xx,yy = random.choice(listt)
                droid = pygame.Rect(xx, yy, 50, 50)
                droids.append(droid)
        if dtimr>120 and state == 3:
            dtimr = 0
        

        
        kePre = pygame.key.get_pressed()
        if kePre[pygame.K_s] and state == 3:
            hero.y+=6*math.cos(math.radians(anglee))
            hero.x+=6*math.sin(math.radians(anglee))
        if kePre[pygame.K_w] and state == 3:
            hero.y-=6*math.cos(math.radians(anglee))
            hero.x-=6*math.sin(math.radians(anglee))
        if kePre[pygame.K_a] and state == 3:
            if anglee<180:
                anglee+=3
        if kePre[pygame.K_d] and state == 3:
            if anglee>-180:
                anglee-=3
        if kePre[pygame.K_p] and state == 11:
            comm = 0
            state = 3
        if kePre[pygame.K_m] and state == 3:
            comm = 0
            state = 22
        #angle continuous....
        if anglee>177:
            anglee=-177
        if anglee<-177:
            anglee=177

        #border control...
        if hero.x<0:
            hero.x = 0
        if hero.x>650:
            hero.x = 650
        if hero.y<0:
            hero.y = 0
        if hero.y>650:
            hero.y = 650
        #jshield spin
        if jang<361:
            jang+=1
        if jang == 360:
            jang = 0

        heroD.x = hero.x-15
        heroD.y = hero.y-15

        colStop(hero, jshie, 80)
        colStop(hero, Tbase, 50)
        for droid in droids:
            if interB(droid, jshie, 65) == True:
                ssta-=1
                droids.remove(droid)
        if ssta == 0:
            comm = 0
            state = 111
            
        fireCheckBu(vBullets, bullets, droids, hero, ang, vang, heroD, jsD, state)
        draw_window(hero, anglee, bullets, vBullets, ang, pri, Tbase, vang, jshie, jang, droids, state, playe, hs1, hs2, hs3, score, health, ssta, comm)

    f = open("hsdat.csv", "w")
    data = [[hs1],[hs2],[hs3]]
    fwrite = csv.writer(f)
    fwrite.writerows(data)
    f.close()

if __name__== "__main__":
    main()