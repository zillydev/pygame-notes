import pygame, sys, os, random
from pygame.locals import *
from player import Player
from block import Block
from bullet import Bullet

pygame.init()

screen_width = 700
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height), SCALED, vsync=True)

pygame.display.set_caption('Block Shooter')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

player_width = 30
player_height = 20

player = Player((screen_width / 2) - (player_width / 2), screen_height - (2 * player_height), player_width, player_height)

blocks = []
block_width = 10
block_height = 10

for _ in range(50):
    block_x = random.randint(int(player_width / 2), screen_width - int(player_width / 2))
    block_y = random.randint(0, screen_height - (4 * player_height))
    blocks.append(Block(block_x, block_y, block_width, block_height))

bullets = []
bullet_width = 5
bullet_height = 10

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bullet_x = (player.rect.x + (player_width / 2)) - (bullet_width / 2)
                bullet_y = player.rect.y - bullet_height
                bullets.append(Bullet(bullet_x, bullet_y, bullet_width, bullet_height))

    keys = pygame.key.get_pressed()

    player.movement[0] = keys[K_d] - keys[K_a]
    player.movement[1] = keys[K_s] - keys[K_w]

    player.rect.x += player.movement[0] * player.velocity
    if player.rect.x < 0:
        player.rect.x = 0
    elif player.rect.x + player_width > screen_width:
        player.rect.x = screen_width - player_width

    for bullet in bullets:
        bullet.rect.y -= bullet.velocity

        if bullet.rect.y + bullet_height < 0:
            bullets.remove(bullet)

        else:
            remove_bullet = False
            for block in blocks:
                if bullet.rect.colliderect(block.rect):
                    remove_bullet = True
                    blocks.remove(block)
            
            if remove_bullet:
                bullets.remove(bullet)


    screen.fill(white)

    
    for block in blocks:
        pygame.draw.rect(screen, red, block.rect)

    for bullet in bullets:
        pygame.draw.rect(screen, black, bullet.rect)

    pygame.draw.rect(screen, green, player.rect)

    pygame.display.update()

    pygame.time.Clock().tick(60)
