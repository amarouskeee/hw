import pygame as pg
from pygame.draw import *





pg.init()

screen = pg.display.set_mode((255, 255))

blue = pg.Сolor(10,52,255)
size = (50,50)
rect= pg.Surface(255,255)
pg.draw.rect(rect,blue,rect.get_rect(),  10)



pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True