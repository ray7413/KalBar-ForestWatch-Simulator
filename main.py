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

mx, my, mx0, my0, dmx, dmy = 0


running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                left_click = True

            elif event.button == 3:

                right_click = True

        elif event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1:
            
                left_click = False

            elif event.button == 3:

                right_click = False

        elif event.type == pygame.MOUSEMOTION:

            mx, my = event.pos

    if left_click:

        ...

    forest_map.render(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
