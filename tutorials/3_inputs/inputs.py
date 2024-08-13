'''
There are two ways of listening to key-based inputs in pygame -
    1. `pygame.key.get_pressed()` : returns the state of every key every frame. Useful for things that require continuous input, like movement.
    2. `event.type == KEYDOWN/KEYUP` : triggered only once when a key is either pressed down or lifted up. Useful for one-time things, like jumping.
List of keys and their keycodes - https://pyga.me/docs/ref/key.html#key-constants-label
'''


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
            '''
            Triggered only once when a key is pressed down.
            '''


            if event.key == K_a:
                '''
                Check for a specific key.
                '''


        if event.type == KEYUP:
            '''
            Triggered only once when a key that was pressed down, is lifted up.
            '''


            if event.key == K_a:
                '''
                Check for a specific key.
                '''



    keys = pygame.key.get_pressed()
    '''
    Populates a dict of currently pressed down keys.
    '''

    if keys[K_a]:
        '''
        Check if a specific key is present in the dict.
        '''


    screen.fill(white)
    

    pygame.display.update()

    pygame.time.Clock().tick(60)
