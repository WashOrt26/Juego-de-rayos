import pygame
from pygame.locals import *
import math

pygame.init()

# Definición de alto y ancho de la ventana
screen_width = 480
screen_height = 360
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simulador de rayo')

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Cargando imágenes y definiendo variables
fondo2 = pygame.image.load('imagenes/Fondo2.png')
fondo2 = pygame.transform.scale(fondo2, (480, 360))

snoopy_avion = pygame.image.load('imagenes/AvionSnoopy.png')
snoopy_avion = pygame.transform.scale(snoopy_avion, (100, 100))

pajaritos = pygame.image.load('imagenes/Pajaritos.png')
pajaritos = pygame.transform.scale(pajaritos, (150, 50))  # Ajustado tamaño del cartel de pajaritos

# Posición inicial de Snoopy en el piso
posicion_x_avion = screen_width // 6 - 50
posicion_y_avion = screen_height - 120

# Posición de los pajaritos en el centro
posicion_x_pajaritos = screen_width // 2 - 75  # Ajustado al nuevo tamaño
posicion_y_pajaritos = screen_height // 2 - 25  # Ajustado al nuevo tamaño

# Velocidades
tiempo_parabolico = 0
velocidad_inicial_avion = 5
gravedad = 0.2  # Gravedad para el movimiento parabólico
angulo_lanzamiento = 45 * (math.pi / 180)  # 45 grados convertido a radianes
vuelo_iniciado = False

velocidad_pajaritos = 2  # Velocidad con la que los pajaritos suben

# Variables del juego
snoopy_volando = False
pajaritos_visible = True  # Para mostrar o esconder los pajaritos
pajaritos_volando = False  # Para iniciar el vuelo de los pajaritos

# Ciclo principal
run = True
while run:
    screen.blit(fondo2, (0, 0))

    # Mostrar a los pajaritos si aún no han sido tocados
    if pajaritos_visible:
        screen.blit(pajaritos, (posicion_x_pajaritos, posicion_y_pajaritos))

    # Movimiento parabólico de SnoopyAvion cuando empieza
    if snoopy_volando:
        tiempo_parabolico += 0.1  # Incremento del tiempo para calcular la posición
        posicion_x_avion += velocidad_inicial_avion * math.cos(angulo_lanzamiento)
        posicion_y_avion -= (velocidad_inicial_avion * math.sin(angulo_lanzamiento)) - (gravedad * tiempo_parabolico**2) / 2

        # Si el avión sale de la pantalla, restablecer la posición
        if posicion_x_avion > screen_width or posicion_y_avion > screen_height:
            posicion_x_avion = screen_width // 6 - 50
            posicion_y_avion = screen_height - 120
            tiempo_parabolico = 0
            snoopy_volando = False

    # Movimiento de los pajaritos hacia arriba cuando vuelan
    if pajaritos_volando:
        posicion_y_pajaritos -= velocidad_pajaritos  # Los pajaritos suben
        if posicion_y_pajaritos + 50 < 0:  # Si los pajaritos salen de la pantalla
            pajaritos_visible = False  # Dejar de mostrar los pajaritos

    # Dibujar a SnoopyAvion en su nueva posición
    screen.blit(snoopy_avion, (posicion_x_avion, posicion_y_avion))

    # Verificar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Detectar clic en los pajaritos para iniciar el vuelo
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if pajaritos_visible:
                # Si se presiona en el área de los pajaritos, inicia el vuelo de Snoopy y los pajaritos
                if (posicion_x_pajaritos) < mouse_pos[0] < (posicion_x_pajaritos + 150) and (posicion_y_pajaritos) < mouse_pos[1] < (posicion_y_pajaritos + 50):
                    snoopy_volando = True  # Iniciar el vuelo parabólico de Snoopy
                    pajaritos_volando = True  # Hacer que los pajaritos vuelen hacia arriba

    pygame.display.flip()

pygame.quit()