from doodle import Doodle
import pygame as pg

pg.init()
pg.font.init()

font = pg.font.SysFont('Name', 100)

W, H = 600, 600


screen = pg.display.set_mode((W, H))
screen.fill(('white'))

doodle = Doodle(300, 300)
all_sprite = pg.sprite.Group(doodle)


run = True

clock = pg.time.Clock()

"""back_ground_img = pg.image.load('doodle.png')
back_ground = pg.surface.Surface((back_ground_img.get_width(), 600))
back_ground_y = 0
back_ground_y2 = back_ground_img.get_width()"""


while run:


    screen.fill('white')
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    all_sprite.draw(screen)
    all_sprite.update()

    pg.display.update()