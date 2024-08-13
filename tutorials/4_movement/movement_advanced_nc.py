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

image_velocity = 5

image_movement = [0, 0]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    image_movement[0] = keys[K_d] - keys[K_a]
    image_movement[1] = keys[K_s] - keys[K_w]

    image_rect.x += image_movement[0] * image_velocity
    image_rect.y += image_movement[1] * image_velocity


    screen.fill(white)
    

    screen.blit(image, image_rect)

    pygame.display.update()

    pygame.time.Clock().tick(60)
