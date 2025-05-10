import pygame as pg

bird_images = [pg.image.load(f'doodle.png') for i in range(1, 4)]


class Doodle(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load(f'doodle.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.vector = 3
        self.jump_time = None

    def jump(self):
        self.vector = 4
        self.jump_time = pg.time.get_ticks()

    def update(self):
        self.rect.y += self.vector
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x -= 3
        if keys[pg.K_RIGHT]:
            self.rect.x += 3


