import pygame
from map import forestMap
from assets.asset import load as load


pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("KalBar ForestWatch Simulator")

clock = pygame.time.Clock()

load()
forest_map = forestMap()
forest_map.generate()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    forest_map.render(screen)

    pygame.display.flip()
    clock.tick(99)

pygame.quit()
