
import pygame as pg



class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load(f'platform.png')
        self.rect = self.image.get_rect(center=(x, y))

