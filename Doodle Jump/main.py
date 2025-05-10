import random
from random import randint

from doodle import Doodle
from platform import Platform
import pygame as pg


velocity_y = 0
gravity = 0.5
jump_power = -10
pg.init()
pg.font.init()

font = pg.font.SysFont('Name', 100)

W, H = 600, 600

screen = pg.display.set_mode((W, H))
screen.fill(('white'))

doodle = Doodle(300, 300)
all_sprite = pg.sprite.Group(doodle)
platform = Platform(300, 550)
all_sprite.add(platform)
platforms = pg.sprite.Group(platform)

jump_time = None

run = True

clock = pg.time.Clock()


def random_platform(count):
    y = 600
    platform_r = Platform(300, 100)
    all_sprite.add(platform_r)
    platforms.add(platform_r)
    mem_random_x = 300 + randint(-120, 120)
    for i in range(count):
        y -= 100
        mem_random_x = mem_random_x + randint(-120, 120)
        platform_r = Platform(mem_random_x, y)
        all_sprite.add(platform_r)
        platforms.add(platform_r)


random_platform(10)


def kill_platform():
    for sprite in platforms:
        sprite.kill()


back_ground_img = pg.image.load('background.png')
back_ground = pg.surface.Surface((back_ground_img.get_width(), 600))
back_ground_y = 0
back_ground_y2 = back_ground_img.get_width()





while run:
    screen.fill('white')
    clock.tick(60)

    back_ground.blit(back_ground_img, (0, 0))
    screen.blit(back_ground, (back_ground_y, 0))
    screen.blit(back_ground, (back_ground_y2, 0))

    back_ground_y = 1
    back_ground_y2 = 1

    if back_ground_y < -back_ground_img.get_width():
        back_ground_y = back_ground_img.get_width()

    if back_ground_y2 < -back_ground_img.get_width():
        back_ground_y2 = back_ground_img.get_width()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False



    if jump_time is not None:
        elapsed_time = pg.time.get_ticks() - jump_time
        if elapsed_time >= 400:
            doodle.vector = 3
            jump_time = None

    for p in platforms:
        if doodle.vector > 0:
            if doodle.rect.colliderect(p.rect):
                if p.rect.top + 10 >= doodle.rect.bottom >= p.rect.top - 10:
                    doodle.vector -= 10
                    jump_time = pg.time.get_ticks()

    if doodle.rect.y < 0:
        doodle.rect.y = 300
        kill_platform()
        random_platform(5)

    all_sprite.draw(screen)
    all_sprite.update()

    pg.display.update()
