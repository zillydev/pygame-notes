import pygame, sys, os
from pygame.locals import *

pygame.init()

screen_width = 400
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height), SCALED, vsync=True)

pygame.display.set_caption('Hello World!')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

def get_relative_path(path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)

image = pygame.image.load(get_relative_path('bird.png'))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    screen.fill(white)
    

    pygame.draw.rect(screen, red, (100, 100, 200, 150))

    screen.blit(image, (200, 200))

    pygame.display.update()

    pygame.time.Clock().tick(60)
