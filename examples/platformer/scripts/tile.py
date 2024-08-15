import pygame

class Tile:
    def __init__(self, x, y, image):
        self.sprite = image
        self.rect = pygame.Rect(x, y, image.get_width(), image.get_height())
