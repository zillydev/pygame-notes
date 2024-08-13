import pygame

class Pipe:
    def __init__(self, image, x, y, height, isUpperPipe):
        self.sprite = pygame.transform.scale(image, (image.get_width(), height))
        if isUpperPipe:
            self.sprite = pygame.transform.flip(self.sprite, False, True)
            
        self.rect = pygame.Rect(x, y, self.sprite.get_width(), height)
        self.velocity = -5
