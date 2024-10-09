import pygame
from pygame.locals import *

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

#Cargando imagenes
fondo2 = pygame.image.load('imagenes/Fondo2.png')

snoopy_caminando_1 = pygame.image.load('imagenes/Sprites_snoopy/Snoopy_caminando_1.png')
snoopy_caminando_2 = pygame.image.load('imagenes/Sprites_snoopy/Snoopy_caminando_2.png')
snoopy_caminando_13 = pygame.image.load('imagenes/Sprites_snoopy/Snoopy_caminando_3.png')


#Fondos
screen.blit(fondo2, (0,0))
pygame.display.flip()

screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('plataformer')

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()