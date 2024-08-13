'''
Graphics in pygame are usually positioned with respect to their top-left corner's coordinate.
Order of rendering should be kept in mind - a graphic drawn first can be underlayed by a graphic drawn after it.
'''


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
'''
Function to get path of an asset relative to the current file
'''


image = pygame.image.load(get_relative_path('bird.png'))
'''
Loads an image and stores it.
'''


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    screen.fill(white)
    '''
    Graphics should always be drawn after filling (clearing) the screen. If drawn before, they would just be cleared, and they won't be visible.
    '''


    pygame.draw.rect(screen, red, (100, 100, 200, 150))
    '''
    Draws a rectangle. Takes three arguments -
        1. Screen surface
        2. Color
        3. Rect tuple, having 4 values - x-coord, y-coord (of top-left corner), width, height
    More shapes available to draw - https://pyga.me/docs/ref/draw.html
    '''


    screen.blit(image, (200, 200))
    '''
    Blit (draw) an image onto the screen. Takes two parameters -
        1. The loaded image to blit
        2. Tuple having 2 values - x-coord, y-coord (of top-left corner)
    '''


    pygame.display.update()

    pygame.time.Clock().tick(60)
