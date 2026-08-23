import random
import pygame
from assets.asset import stamp

WIDTH = 20
HEIGHT = 20

TILE_WIDTH = 64
TILE_HEIGHT = 32

def grid_to_screen(x, y, offset_x=0, offset_y=0):

    screen_x = (x - y) * (TILE_WIDTH // 2) + offset_x
    screen_y = (x + y) * (TILE_HEIGHT // 2) + offset_y

    return screen_x, screen_y

class forestMap:

    def __init__(self):

        self.tiles = []

        self.offsetx = 200
        self.offsety = 50

    def generate(self):

        for y in range(HEIGHT):

            columns = []

            for x in range(WIDTH):

                columns.append("forest")

            self.tiles.append(columns)

    def render(self, screen):

        for y in range(len(self.tiles)):

            for x in range(len(self.tiles[y])):

                tile_type = self.tiles[y][x]

                screen_x, screen_y = grid_to_screen(x, y, 50, 50)
                stamp(screen, tile_type, screen_x, screen_y)