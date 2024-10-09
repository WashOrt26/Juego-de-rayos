import pygame
from pygame.locals import *
import random

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simulador de rayo')

#Cargando imagenes y definiendo variables
fondo2 = pygame.image.load('imagenes/Fondo2.png')

nube1 = pygame.image.load('imagenes/Nube1.png')
nube1 = pygame.transform.scale(nube1,(150,105))

snoopy_caminando_1 = pygame.image.load('imagenes/Sprites_snoopy/Snoopy_caminando_1.png')
snoopy_caminando_2 = pygame.image.load('imagenes/Sprites_snoopy/Snoopy_caminando_2.png')
snoopy_caminando_13 = pygame.image.load('imagenes/Sprites_snoopy/Snoopy_caminando_3.png')

casita_snopy = pygame.image.load('imagenes/Casita_snoopy.png')
casita_snopy = pygame.transform.scale(casita_snopy,(125,150))

#Definir posición inicial y final de la nube y velocidad
initial_x = 0
initial_y = 0
final_x = 640
final_y = 480

velocidad = 2
#Fondos
screen.blit(fondo2, (0,0))
pygame.display.flip()

pygame.display.set_caption('Simulador de rayos')

posicion_x = random.randint(0, screen_width - 150)
posicion_y = 50

run = True

while run:

    screen.blit(fondo2, (0,0))
    screen.blit(casita_snopy, (340,290))
    screen.blit(nube1, (posicion_x, posicion_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()