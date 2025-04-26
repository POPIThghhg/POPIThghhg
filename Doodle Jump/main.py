from sys import platform

from doodle import Doodle
from platform import Platform
import pygame as pg

pg.init()
pg.font.init()

font = pg.font.SysFont('Name', 100)

W, H = 600, 600


screen = pg.display.set_mode((W, H))
screen.fill(('white'))

doodle = Doodle(300, 300)
all_sprite = pg.sprite.Group(doodle)
platform = Platform(100, 100, 100, 25)
all_sprite.add(platform)


run = True

clock = pg.time.Clock()


while run:


    screen.fill('white')
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False


    if pg.sprite.spritecollide(doodle, platform, False):
        run = False




    all_sprite.draw(screen)
    all_sprite.update()

    pg.display.update()