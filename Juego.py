import pygame
from pygame.locals import *
import random

pygame.init()
# Definición de alto y ancho de la ventana
screen_width = 480
screen_height = 360
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simulador de rayo')

#Cargando imagenes y definiendo variables
fondo2 = pygame.image.load('imagenes/Fondo2.png')
fondo2 = pygame.transform.scale(fondo2,(480,360))

nube1 = pygame.image.load('imagenes/Nube1.png')
nube1 = pygame.transform.scale(nube1,(153,82))

snoopy_caminando_1 = pygame.image.load('imagenes/Sprites_snoopy/Snoopy_caminando_1.png')
snoopy_caminando_1 = pygame.transform.scale(snoopy_caminando_1,(80,120))
snoopy_caminando_2 = pygame.image.load('imagenes/Sprites_snoopy/Snoopy_caminando_2.png')
snoopy_caminando_2 = pygame.transform.scale(snoopy_caminando_2,(80,120))
snoopy_caminando_3 = pygame.image.load('imagenes/Sprites_snoopy/Snoopy_caminando_3.png')
snoopy_caminando_3 = pygame.transform.scale(snoopy_caminando_2,(80,120))
snoopy_caminando = [snoopy_caminando_1,snoopy_caminando_2,snoopy_caminando_3]

casita_snopy = pygame.image.load('imagenes/Casita_snoopy.png')
casita_snopy = pygame.transform.scale(casita_snopy,(124,150))

#Fondos
screen.blit(fondo2, (0,0))
pygame.display.flip()


#Posición aleatoria de la nube en x al iniciar y posicion x snooopy
posicion_x = random.randint(0, screen_width - 150)
posicion_y = 50

posicion_x_snoopy = random.randint(0, screen_width - 150)
posicion_y_snoopy = 220

#Velocidad de movimiento de la nube y snoopy
velocidad_nube = 0.2

velocidad_snoopy = 0.5

#Dirección nube y snoopy
direccion_nube = 1
direccion_snoopy = 1

#Animacion snoopy
indice_snoopy = 0
contador_animacion_snoopy = 0
velocidad_animacion_snoopy = 50

mirando_derecha = True

run = True
# CICLO
while run:


    screen.blit(fondo2, (0,0))
    screen.blit(casita_snopy, (340,178))
    screen.blit(nube1, (posicion_x, posicion_y))
    

    #Posicion nube
    posicion_x += velocidad_nube * direccion_nube
    if posicion_x <= 0 or posicion_x >= screen_width - 153:
        direccion_nube *= -1

    #Posicion snoopy
    posicion_x_snoopy += velocidad_snoopy * direccion_snoopy
    if posicion_x_snoopy <= 0 or posicion_x_snoopy >= screen_width - 90:
        direccion_snoopy *= -1
        mirando_derecha = not mirando_derecha

    #Animacion de snoopy

    contador_animacion_snoopy += 1
    if contador_animacion_snoopy >= velocidad_animacion_snoopy:
        contador_animacion_snoopy = 0
        indice_snoopy = (indice_snoopy +1) % len(snoopy_caminando)
    
    if mirando_derecha:
        screen.blit(snoopy_caminando[indice_snoopy],(posicion_x_snoopy, posicion_y_snoopy))
    else:
        snoopy_volteado = pygame.transform.flip(snoopy_caminando[indice_snoopy], True, False)
        screen.blit(snoopy_volteado, (posicion_x_snoopy, posicion_y_snoopy))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()


pygame.quit()