import pygame
from pygame.locals import *

pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('plataformer')

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


