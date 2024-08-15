import pygame, sys, os
from pygame.locals import *
from tile import Tile
from tilemap import Tilemap
from utils import get_relative_path
from player import Player

pygame.init()

tmap = Tilemap('../tilemaps/tilemap.json')

tiles = tmap.init_tiles()

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height), SCALED, vsync=True)
display = pygame.Surface((tmap.width * tmap.tile_width, tmap.height * tmap.tile_height))


pygame.display.set_caption('Platformer')

clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

tile_surf = pygame.Surface(display.get_size())
tile_surf.fill(white)

for tile in tiles:
    tile_surf.blit(tile.sprite, tile.rect)

player_sprite = pygame.image.load(get_relative_path('../assets/player/0.png'))
player_scroll_offset = 100
player = Player(player_scroll_offset, 0, player_sprite)

scroll = [0, 0]

gravity = 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.velocity[1] = -20

    scroll[0] = -player.rect.x

    keys = pygame.key.get_pressed()
    
    player.movement[0] = keys[K_d] - keys[K_a]

    player.velocity[0] = player.movement[0] * 5
    player.velocity[1] += gravity

    player.rect.x += player.velocity[0]
    for tile in tiles:
        if player.rect.colliderect(tile.rect):
            if player.velocity[0] < 0:
                player.rect.left = tile.rect.right
            elif player.velocity[0] > 0:
                player.rect.right = tile.rect.left

    player.rect.y += player.velocity[1]
    for tile in tiles:
        if player.rect.colliderect(tile.rect):
            if player.velocity[1] < 0:
                player.rect.top = tile.rect.bottom
            elif player.velocity[1] > 0:
                player.rect.bottom = tile.rect.top
            player.velocity[1] = 0


    display.fill(white)


    display.blit(tile_surf, (scroll[0] + player_scroll_offset,0))

    display.blit(player.sprite, (player_scroll_offset, player.rect.y))

    screen.blit(pygame.transform.scale(display, (tmap.width * tmap.tile_width, screen_height)), (0, 0))


    pygame.display.update()

    clock.tick(60)
