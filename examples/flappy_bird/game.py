import pygame, sys, os, random
from pygame.locals import *
from player import Player
from pipe import Pipe
from utils import get_relative_path

pygame.init()

screen_width = 600
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height), SCALED, vsync=True)

pygame.display.set_caption('Flappy Bird')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

player_image = pygame.image.load(get_relative_path('bird.png'))
player_width = player_image.get_width()
player_height = player_image.get_height()

player = Player(100, (screen_height / 2) - (player_height / 2), player_width, player_height)

pipe_image = pygame.image.load(get_relative_path('pipe.png'))
pipe_gap = 150

pipes = []

def create_pipes():
    pipe_1_height = random.randint(0, screen_height - (int(screen_height / 2)))
    pipe_2_height = screen_height - (pipe_1_height + pipe_gap)
    pipe_1 = Pipe(pipe_image, screen_width, 0, pipe_1_height, True)
    pipe_2 = Pipe(pipe_image, screen_width, pipe_1_height + pipe_gap, pipe_2_height, False)
    pipes.append(pipe_1)
    pipes.append(pipe_2)

ADD_PIPE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_PIPE_EVENT, 1200)

gravity = 1

done = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.velocity = -15
        if event.type == ADD_PIPE_EVENT:
            create_pipes()

    keys = pygame.key.get_pressed()

    player.velocity += gravity
    player.rect.y += player.velocity
    
    if player.rect.y < 0 or player.rect.y + player_height > screen_height:
        done = True

    pipes_to_remove = []
    for pipe in pipes:
        pipe.rect.x += pipe.velocity

        if pipe.rect.colliderect(player.rect):
            done = True

        if pipe.rect.x + pipe.rect.width < 0:
            pipes_to_remove.append(pipe)

    for pipe in pipes_to_remove:
        pipes.remove(pipe)


    screen.fill(white)


    for pipe in pipes:
        screen.blit(pipe.sprite, pipe.rect)

    screen.blit(player_image, player.rect)

    pygame.display.update()

    pygame.time.Clock().tick(60)
