import pygame
import time



def load():

    global burning, burnt, forest

    burning = pygame.image.load("assets/burning.png").convert_alpha()
    burnt = pygame.image.load("assets/burnt.png").convert_alpha()
    forest = pygame.image.load("assets/forest.png").convert_alpha()

def stamp(screen, object, x, y):

    match object:

        case "burning":

            screen.blit(burning, (x,y))

        case "burnt":

            screen.blit(burnt, (x,y))

        case "forest":

            screen.blit(forest, (x,y))