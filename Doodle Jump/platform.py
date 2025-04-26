
import pygame as pg
from Tools.demo.spreadsheet import center


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))

