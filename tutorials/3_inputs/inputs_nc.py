import pygame, sys
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

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                pass

        if event.type == KEYUP:
            if event.key == K_a:
                pass

    keys = pygame.key.get_pressed()

    if keys[K_a]:
        pass


    screen.fill(white)
    

    pygame.display.update()

    pygame.time.Clock().tick(60)
