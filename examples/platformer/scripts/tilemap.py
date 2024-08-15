import json, os, pygame
from utils import get_relative_path
from tile import Tile

class Tilemap:
    def __init__(self, path):
        with open(get_relative_path(path)) as file:
            data = json.load(file)

        self.map = data['tilemap']
        self.width = data['width']
        self.height = data['height']
        self.tile_width = data['tile_width']
        self.tile_height = data['tile_height']
        self.tilesets = {}
        self.load_tilesets()

    def init_tiles(self):
        tiles = []
        for tile in self.map:
            new_tile = Tile(tile['x'] * self.tile_width, tile['y'] * self.tile_height, self.tilesets[tile['type']][tile['id']])
            tiles.append(new_tile)
        
        return tiles

    def load_tilesets(self):
        types = os.listdir(get_relative_path('../assets/tiles'))
        for t in types:
            self.tilesets[t] = []
            tiles = os.listdir(get_relative_path(f'../assets/tiles/{t}'))
            for tile in tiles:
                self.tilesets[t].append(pygame.image.load(get_relative_path(f'../assets/tiles/{t}/{tile}')))
