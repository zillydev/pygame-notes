import pygame

class Player:
    def __init__(self, x, y, sprite):
        self.rect = pygame.Rect(x, y, sprite.get_width(), sprite.get_height())
        self.sprite = sprite
        self.movement = [0,0]
        self.velocity = [0,0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}