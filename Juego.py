import random

import pygame

pygame.init()

# Definición de alto y ancho de la ventana
screen_width = 480
screen_height = 360
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simulador de rayo')

# Cargando imágenes y definiendo variables
fondo2 = pygame.image.load('imagenes/Fondo2.png')
fondo2 = pygame.transform.scale(fondo2, (480, 360))

nube1 = pygame.image.load('imagenes/Nube1.png')
nube1 = pygame.transform.scale(nube1, (153, 82))

snoopy_caminando_1 = pygame.image.load('imagenes/Sprites_snoopy/Snoopy_caminando_1.png')
snoopy_caminando_1 = pygame.transform.scale(snoopy_caminando_1, (80, 120))
snoopy_caminando_2 = pygame.image.load('imagenes/Sprites_snoopy/Snoopy_caminando_2.png')
snoopy_caminando_2 = pygame.transform.scale(snoopy_caminando_2, (80, 120))
snoopy_caminando_3 = pygame.image.load('imagenes/Sprites_snoopy/Snoopy_caminando_3.png')
snoopy_caminando_3 = pygame.transform.scale(snoopy_caminando_3, (80, 120))
snoopy_caminando = [snoopy_caminando_1, snoopy_caminando_2, snoopy_caminando_3]


#Woodstock
woodstock_caminando_1 = pygame.image.load('imagenes/Sprites_woodstock/woodstock_caminando_1.png')
woodstock_caminando_1 = pygame.transform.scale(woodstock_caminando_1, (40, 40))
woodstock_caminando_2 = pygame.image.load('imagenes/Sprites_woodstock/woodstock_caminando_2.png')
woodstock_caminando_2 = pygame.transform.scale(woodstock_caminando_2, (40, 40))
woodstock_caminando_3 = pygame.image.load('imagenes/Sprites_woodstock/woodstock_caminando_3.png')
woodstock_caminando_3 = pygame.transform.scale(woodstock_caminando_3, (40, 40))
woodstock_caminando = [woodstock_caminando_1, woodstock_caminando_2, woodstock_caminando_3]

woodstock_estatico_1 = pygame.image.load('imagenes/Sprites_woodstock/woodstock_estatico_1.png')
woodstock_estatico_1 = pygame.transform.scale(woodstock_estatico_1, (40, 40))

# Cargando los botones de interrogación
interrogacion = pygame.image.load('imagenes/interrogacion.png')
interrogacion = pygame.transform.scale(interrogacion, (30, 30))
interrogacion_hover = pygame.image.load('imagenes/interrogacion_hover.png')
interrogacion_hover = pygame.transform.scale(interrogacion_hover, (30, 30))
interrogacion_gris = pygame.image.load('imagenes/interrogacion_gris.png')
interrogacion_gris = pygame.transform.scale(interrogacion_gris, (30, 30))

# Posición del botón de interrogación
boton_interrogacion_pos = (screen_width - 40, 10)

# Variables para controlar el estado del botón y Woodstock
boton_interrogacion_activo = True
woodstock_movimiento = False
woodstock_x = -50  # Posición inicial fuera de la pantalla
woodstock_contador = 0
woodstock_animacion = 0
woodstock_hablando = False
mensaje = "Hola, soy Woodstock."

casita_snopy = pygame.image.load('imagenes/Casita_snoopy.png')
casita_snopy = pygame.transform.scale(casita_snopy, (124, 150))

# Botones de rayos (gris deshabilitado) y separador de cargas
imagen_rayo_gris = pygame.image.load('imagenes/rayo_gris.png')
imagen_rayo_gris = pygame.transform.scale(imagen_rayo_gris, (60, 60))
rayo_pos = (10, 20)  # Posición del botón de rayo

separador_cargas_1 = pygame.image.load('imagenes/separador_cargas_1.png')
separador_cargas_2 = pygame.image.load('imagenes/separador_cargas_2.png')
imagen_separador_normal = pygame.transform.scale(separador_cargas_1, (60, 60))
imagen_separador_hover = pygame.transform.scale(separador_cargas_2, (60, 60))

boton_separador_pos = (10, 85)

# Cargar imágenes de las cargas positivas y negativas
carga_positiva_img = pygame.image.load('imagenes/carga_positiva.png')
carga_positiva_img = pygame.transform.scale(carga_positiva_img, (20, 20))  # Tamaño de la carga positiva
carga_negativa_img = pygame.image.load('imagenes/carga_negativa.png')
carga_negativa_img = pygame.transform.scale(carga_negativa_img, (20, 20))  # Tamaño de la carga negativa

# Generar posiciones aleatorias de las cargas positivas en el suelo
cantidad_cargas_suelo = 20  # Número de cargas positivas en el suelo
cargas_suelo = []

for _ in range(cantidad_cargas_suelo):
    posicion_x_carga = random.randint(0, screen_width - 40)  # Posición aleatoria en x
    posicion_y_carga = screen_height - 40  # Suelo (posición fija en y)
    cargas_suelo.append((posicion_x_carga, posicion_y_carga))

# Generar posiciones aleatorias y movimiento de las cargas dentro de la nube
cantidad_cargas_nube = 10  # Número de cargas positivas y negativas dentro de la nube
cargas_en_nube = []

for _ in range(cantidad_cargas_nube):
    # Posiciones relativas a la nube
    posicion_x_carga = random.randint(0, 153 - 20)  # Dentro del área de la nube
    posicion_y_carga = random.randint(0, 82 - 20)
    velocidad_x_carga = random.choice([-2.5, 2.5]) * random.uniform(0.1, 0.3)  # Movimiento aleatorio en x
    velocidad_y_carga = random.choice([-2.5, 2.5]) * random.uniform(0.1, 0.3)  # Movimiento aleatorio en y
    # Elegir aleatoriamente si la carga es positiva o negativa
    tipo_carga = random.choice([carga_positiva_img, carga_negativa_img])
    cargas_en_nube.append([tipo_carga, posicion_x_carga, posicion_y_carga, velocidad_x_carga, velocidad_y_carga])
def escena_simulador():
    global woodstock_movimiento, woodstock_x, woodstock_contador, woodstock_animacion, woodstock_hablando, boton_interrogacion_activo
    posicion_x_nube = random.randint(0, screen_width - 153)
    posicion_y_nube = 50

    posicion_x_snoopy = random.randint(0, screen_width - 150)
    posicion_y_snoopy = 220

    velocidad_nube = 0.2
    velocidad_snoopy = 0.5
    direccion_nube = 1
    direccion_snoopy = 1
    indice_snoopy = 0
    contador_animacion_snoopy = 0
    velocidad_animacion_snoopy = 50
    mirando_derecha = True
    run = True

    while run:
        screen.blit(fondo2, (0, 0))
        screen.blit(casita_snopy, (340, 178))
        screen.blit(nube1, (posicion_x_nube, posicion_y_nube))

        for carga in cargas_suelo:
            screen.blit(carga_positiva_img, carga)

        for carga in cargas_en_nube:
            tipo_carga, carga_x, carga_y, velocidad_x, velocidad_y = carga
            carga_x += velocidad_x
            carga_y += velocidad_y
            if carga_x <= 0 or carga_x >= 153 - 20:
                velocidad_x *= -1
            if carga_y <= 0 or carga_y >= 82 - 20:
                velocidad_y *= -1
            screen.blit(tipo_carga, (posicion_x_nube + carga_x, posicion_y_nube + carga_y))
            carga[1] = carga_x
            carga[2] = carga_y
            carga[3] = velocidad_x
            carga[4] = velocidad_y

        posicion_x_nube += velocidad_nube * direccion_nube
        if posicion_x_nube <= 0 or posicion_x_nube >= screen_width - 153:
            direccion_nube *= -1

        posicion_x_snoopy += velocidad_snoopy * direccion_snoopy
        if posicion_x_snoopy <= 0 or posicion_x_snoopy >= screen_width - 90:
            direccion_snoopy *= -1
            mirando_derecha = not mirando_derecha

        contador_animacion_snoopy += 1
        if contador_animacion_snoopy >= velocidad_animacion_snoopy:
            contador_animacion_snoopy = 0
            indice_snoopy = (indice_snoopy + 1) % len(snoopy_caminando)

        if mirando_derecha:
            screen.blit(snoopy_caminando[indice_snoopy], (posicion_x_snoopy, posicion_y_snoopy))
        else:
            snoopy_volteado = pygame.transform.flip(snoopy_caminando[indice_snoopy], True, False)
            screen.blit(snoopy_volteado, (posicion_x_snoopy, posicion_y_snoopy))

        screen.blit(imagen_rayo_gris, rayo_pos)
        mouse_pos = pygame.mouse.get_pos()

        boton_separador_rect = pygame.Rect(boton_separador_pos, (60, 60))
        if boton_separador_rect.collidepoint(mouse_pos):
            screen.blit(imagen_separador_hover, boton_separador_pos)
        else:
            screen.blit(imagen_separador_normal, boton_separador_pos)

        # Botón de interrogación con funcionalidad
        boton_interrogacion_rect = pygame.Rect(boton_interrogacion_pos, (30, 30))
        if boton_interrogacion_activo:
            if boton_interrogacion_rect.collidepoint(mouse_pos):
                screen.blit(interrogacion_hover, boton_interrogacion_pos)
            else:
                screen.blit(interrogacion, boton_interrogacion_pos)
        else:
            screen.blit(interrogacion_gris, boton_interrogacion_pos)

        # Movimiento de Woodstock
        if woodstock_movimiento:
            woodstock_x += 0.3  # Velocidad de Woodstock
            woodstock_contador += 0.27
            woodstock_animacion = (woodstock_animacion + 1) % len(woodstock_caminando)
            screen.blit(woodstock_caminando[woodstock_animacion], (woodstock_x, screen_height - 70))

            if woodstock_contador >= 120:  # Después de 4 segundos (60 fps * 4)
                woodstock_movimiento = False
                woodstock_hablando = True

        if woodstock_hablando:
            screen.blit(woodstock_estatico_1, (woodstock_x, screen_height - 70))
            # Mostrar el globo de diálogo diagonalmente
            fuente = pygame.font.SysFont('Arial', 16)
            globo_texto = fuente.render(mensaje, True, (0, 0, 0))
            screen.blit(globo_texto, (woodstock_x + 40, screen_height - 100))

        # Procesar eventos de Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and boton_interrogacion_rect.collidepoint(mouse_pos):
                if boton_interrogacion_activo:
                    boton_interrogacion_activo = False
                    woodstock_movimiento = True  # Activar el movimiento de Woodstock
                    # Verificar si se hace clic en el botón separador
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_separador_rect.collidepoint(mouse_pos):
                    return escena_separador()  # Cambia a la nueva escena

        pygame.display.flip()


# Cargando imágenes
fondo_1 = pygame.image.load('imagenes/Fondo_1.png')
fondo_1 = pygame.transform.scale(fondo_1, (480, 360))

nube2 = pygame.image.load('imagenes/Nube1.png')
nube2 = pygame.transform.scale(nube2, (400, 330))

carga_positiva_img2 = pygame.image.load('imagenes/carga_positiva.png')
carga_positiva_img2 = pygame.transform.scale(carga_positiva_img2, (60, 60))  # Tamaño de la carga positiva
carga_negativa_img2 = pygame.image.load('imagenes/carga_negativa.png')
carga_negativa_img2 = pygame.transform.scale(carga_negativa_img2, (60, 60))  # Tamaño de la carga negativa

cantidad_cargas_nube2 = 10  # Número de cargas positivas y negativas dentro de la nube
cargas_en_nube2 = []

for _ in range(cantidad_cargas_nube2):
    # Posiciones relativas a la nube
    posicion_x_carga2 = random.randint(0, 153 - 20)  # Dentro del área de la nube
    posicion_y_carga2 = random.randint(0, 82 - 20)
    velocidad_x_carga2 = random.choice([-2.5, 2.5]) * random.uniform(0.1, 0.3)  # Movimiento aleatorio en x
    velocidad_y_carga2 = random.choice([-2.5, 2.5]) * random.uniform(0.1, 0.3)  # Movimiento aleatorio en y
    # Elegir aleatoriamente si la carga es positiva o negativa
    tipo_carga2 = random.choice([carga_positiva_img2, carga_negativa_img2])
    cargas_en_nube2.append([tipo_carga2, posicion_x_carga2, posicion_y_carga2, velocidad_x_carga2, velocidad_y_carga2])

fuente_pixel = pygame.font.Font('imagenes/PixelifySans-SemiBold.ttf',20)  # Cambia esto por tu fuente de pixel si la tienes
texto_surface = fuente_pixel.render("Presione esc para saltar", True, (0, 0, 0))
texto_rect = texto_surface.get_rect(topright=(480 - 10, 10))  # Posición arriba a la derecha


def escena_separador():
    global cargas_en_nube2  # Usar la lista global de cargas
    run = True

    while run:
        screen.blit(fondo_1, (0, 0))
        screen.blit(nube2, (35, 10))

        for carga in cargas_en_nube2:
            tipo_carga, carga_x, carga_y, velocidad_x, velocidad_y = carga

            # Actualizar la posición de la carga
            carga_x += velocidad_x
            carga_y += velocidad_y

            # Ajustar la posición vertical lentamente
            if tipo_carga == carga_positiva_img2:
                carga_y -= 0.1  # Las cargas positivas suben lentamente
            else:
                carga_y += 0.1  # Las cargas negativas bajan lentamente

            # Mantener las cargas dentro de los límites de la ventana (480x360)
            if carga_x < 0:
                carga_x = 0  # Limitar el borde izquierdo
                velocidad_x *= -1  # Invertir dirección en x
            elif carga_x > 480 - 60:
                carga_x = 480 - 60  # Limitar el borde derecho
                velocidad_x *= -1  # Invertir dirección en x

            if carga_y < 0:
                carga_y = 0  # Limitar el borde superior
            elif carga_y > 360 - 60:
                carga_y = 360 - 60  # Limitar el borde inferior

            # Verificar colisiones entre cargas
            for otra_carga in cargas_en_nube2:
                if carga != otra_carga:  # Evitar verificar colisión con sí misma
                    tipo_otra_carga, otra_x, otra_y, otra_vel_x, otra_vel_y = otra_carga
                    distancia = ((carga_x - otra_x) ** 2 + (carga_y - otra_y) ** 2) ** 0.5

                    # Verificar si están lo suficientemente cerca para considerarse una colisión
                    if distancia < 60:  # Suponiendo que el tamaño de las cargas es 20x20
                        # Solo reaccionar si son de tipo opuesto
                        if tipo_carga != tipo_otra_carga:
                            # Invertir las direcciones de ambas cargas (efecto de repulsión)
                            velocidad_x *= -1
                            velocidad_y *= -1
                            otra_vel_x *= -1
                            otra_vel_y *= -1

                            # Actualizar las velocidades de la otra carga
                            otra_carga[3] = otra_vel_x
                            otra_carga[4] = otra_vel_y

            # Dibujar la carga actualizada en la pantalla
            screen.blit(tipo_carga, (carga_x, carga_y))

            # Actualizar los valores de la carga en la lista
            carga[1] = carga_x
            carga[2] = carga_y
            carga[3] = velocidad_x
            carga[4] = velocidad_y


        screen.blit(texto_surface, texto_rect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Presiona ESC para volver
                    return escena_simulador()  # Volver a la escena del simulador

        pygame.display.flip()

if __name__ == '__main__':
    escena_simulador()
    pygame.quit()
