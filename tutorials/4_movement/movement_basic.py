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

image_rect = pygame.Rect(200, 200, image.get_width(), image.get_height())
'''
pygame.Rect is a helper class that provides handy methods for movement and collisions.
This by itself does not render anything, it just stores positional data.
It takes four arguments in its constructor -
    1. x-coord
    2. y-coord
    3. width
    4. height
Here we used `image.get_width()` and `image.get_height()` to get the width and height of the loaded image.
'''


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[K_a]:
        image_rect.x -= 5
        '''
        If the a-key is pressed down, move the rect's x-coord by 5 pixels to the left.
        This will happen for every frame the key is pressed, so the image will keep moving left as long as the key is pressed.
        '''
    

    '''
    All game logic like movement should be done before rendering anything, so that the changes are immediately reflected.
    '''
    screen.fill(white)
    

    screen.blit(image, image_rect)
    '''
    Here we pass the rect directly, and it will the obtain the position of the rect and render the image accordingly.
    '''

    pygame.display.update()

    pygame.time.Clock().tick(60)
