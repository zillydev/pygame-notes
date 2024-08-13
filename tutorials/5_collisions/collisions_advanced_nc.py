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

obstacle_rect = pygame.Rect(100, 100, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    image_movement[0] = keys[K_d] - keys[K_a]
    image_movement[1] = keys[K_s] - keys[K_w]

    image_rect.x += image_movement[0] * image_velocity

    if image_rect.colliderect(obstacle_rect):
        if image_movement[0] == -1:
            image_rect.left = obstacle_rect.right

        if image_movement[0] == 1:
            image_rect.right = obstacle_rect.left
    
    
    image_rect.y += image_movement[1] * image_velocity

    if image_rect.colliderect(obstacle_rect):
        if image_movement[1] == -1:
            image_rect.top = obstacle_rect.bottom

        if image_movement[1] == 1:
            image_rect.bottom = obstacle_rect.top



    screen.fill(white)
    

    pygame.draw.rect(screen, red, obstacle_rect)

    screen.blit(image, image_rect)

    pygame.display.update()

    pygame.time.Clock().tick(60)
