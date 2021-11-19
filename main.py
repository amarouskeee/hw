import pygame as pg
from pygame.draw import *





pg.init()

s = pg.display.set_mode((700, 500))
#house
rect(s, (150,180,255),(0,0,700,250))
rect(s, (0,255,0), (0,250,700,250))
rect(s, (155,50,50),(100,200,210,160))
rect(s, (100,170,255),(150,240,90,70))
rect(s, (180,150,180),(150,240,90,70),2)
polygon(s,(255,180,180),[(100,200),(310,200),(205,110),(205,110)])
#tree
circle(s,(0,100,0),(510,120),35)
circle(s,(0,0,0),(510,120),35,1)
circle(s,(0,100,0),(550,160),35)
circle(s,(0,0,0),(550,160),35,1)
circle(s,(0,100,0),(470,160),35)
circle(s,(0,0,0),(470,160),35,1)
rect(s, (0,0,0), (500,230,20,100))
circle(s,(0,100,0),(510,180),35)
circle(s,(0,0,0),(510,180),35,1)
circle(s,(0,100,0),(540,210),35)
circle(s,(0,0,0),(540,210),35,1)
circle(s,(0,105,0),(480,210,),35)
circle(s,(0,0,0),(480,210,),35,1)
#clouds
circle(s,(255,255,255),(100,80),25)
circle(s,(0,0,0),(100,80),25,1)
circle(s,(255,255,255),(120,78),25)
circle(s,(0,0,0),(120,78),25,1)
circle(s,(255,255,255),(140,77),25)
circle(s,(0,0,0),(140,77),25,1)
circle(s,(255,255,255),(160,77),25)
circle(s,(0,0,0),(160,77),25,1)
circle(s,(255,255,255),(140,65),25)
circle(s,(0,0,0),(140,65),25,1)
circle(s,(255,255,255),(110,67),25)
circle(s,(0,0,0),(110,67),25,1)
#sun
circle(s, (255,192,203),(635,70),30)




pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True