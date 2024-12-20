import random

import pygame

import sys
import subprocess  # Para ejecutar otro archivo


pygame.init()
pygame.font.init()

pygame.mixer.init()

pygame.mixer.music.load("musiquita/sonido_fondo.mp3")  # Cargar la música
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)  # Reproducir la música en bucle
# Cargar efectos de sonido
woodstock_camina_sound = pygame.mixer.Sound("musiquita/woodstock_camina.wav")
woodstock_habla_sound = pygame.mixer.Sound("musiquita/woodstock_habla.wav")
snoopy_avisado_sound = pygame.mixer.Sound("musiquita/mmm.wav")  # Cargar el nuevo sonido
rayo_cayendo_sound = pygame.mixer.Sound("musiquita/rayo_cayendo.mp3")  # Cargar el sonido del rayo
asado_sound = pygame.mixer.Sound("musiquita/asado.wav")  # Cargar el sonido de asado


# Definición de alto y ancho de la ventana
screen_width = 480
screen_height = 360
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simulador de rayo')

# Cargando imágenes y definiendo variables
fondo_menu = pygame.image.load("Imagenes/1.png")
fondo_menu = pygame.transform.scale(fondo_menu, (screen_width, screen_height))

# Cargar y escalar el botón (ajustado proporcionalmente)
boton_img = pygame.image.load("Imagenes/Boton.png")
boton_img = pygame.transform.scale(boton_img, (screen_width // 3, screen_height // 4))  # Ajusta el tamaño del botón
boton_rect = boton_img.get_rect(center=(screen_width // 2.2, screen_height // 1.53))

# Resto de las imágenes y variables para el simulador
# (Carga de imágenes, diálogo, etc. como en tu código original)

def menu_principal():
    run = True
    while run:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if boton_rect.collidepoint(evento.pos):
                    escena_simulador()  # Cambiar a la función escena_simulador

        # Dibujar el fondo y el botón
        screen.blit(fondo_menu, (0, 0))
        screen.blit(boton_img, boton_rect)

        pygame.display.flip()


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

dialogos = [
    {"texto": "¡Hola, aquí abajo!", "duracion": 2000},  # 2 segundos
    {"texto": "¡Hey, amigo!", "duracion": 2000},  # 4 segundos
    {"texto": "Mira bien lo \nque pasa\n en el \n cielo", "duracion": 3000},  # 3 segundos
    {"texto": "Esas bolitas\n moradas\n son cargas\n eléctricas.", "duracion": 3000},
    {"texto": "Las que \ntienen un signo\n + son\n positivas,", "duracion": 3000},# 3 segundos
    {"texto": "y las que\n tienen un\n signo - \nson negativas.", "duracion": 3000},  # 3 segundos
    {"texto": "¿Sabías que \nlas \ncargas \nopuestas   se\n   atraen?", "duracion": 3000},  # 3 segundos
    {"texto": "Aún no están\n listas\n para hacer \nun rayo", "duracion": 3000},
    {"texto": "porque están\n todas \nmezcladas.", "duracion": 3000},# 3 segundos
    {"texto": "Pero si\n miras bien, \ndentro de \nesa nube ", "duracion": 2000},
    {"texto": "hay una pelea \nde atracción ", "duracion": 2000},
    {"texto": "entre\n las cargas \n positivas \ny negativas.", "duracion": 2000},# 2 segundos# 3 segundos
    {"texto": "Ummm", "duracion": 2000},
    {"texto": "¿Ves ese \nbotón amarillo\n en el cielo,\n justo ahí?", "duracion": 2000},
    {"texto": "Si lo presionas,\n empezará\n un proceso\n emocionante", "duracion": 2000},
    {"texto": " las cargas\n dentro de\n la nube se van a\n separar.", "duracion": 2000},
    {"texto": " Las positivas \nirán a un lado y\n las negativas al otro.", "duracion": 2000},

]


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
woodstock_movimiento2 = False
woodstock_x = -50  # Posición inicial fuera de la pantalla
woodstock_contador = 0
woodstock_animacion = 0
woodstock_hablando2 = False

# Cargar la imagen del globo de texto
globo_imagen = pygame.image.load('imagenes/globo_texto.png')
globo_imagen = pygame.transform.scale(globo_imagen, (300, 200))  # Ajusta el tamaño según sea necesario

casita_snopy = pygame.image.load('imagenes/Casita_snoopy.png')
casita_snopy = pygame.transform.scale(casita_snopy, (124, 150))

# Botones de rayos (gris deshabilitado) y separador de cargas
imagen_rayo = pygame.image.load('imagenes/rayo.png')
imagen_rayo = pygame.transform.scale(imagen_rayo, (60,60))
imagen_rayo_hover = pygame.image.load('imagenes/rayo_hover.png')
imagen_rayo_hover = pygame.transform.scale(imagen_rayo_hover, (60,60))
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
cargas_suelo3 = []

for _ in range(cantidad_cargas_suelo):
    posicion_x_carga = random.randint(0, screen_width - 40)  # Posición aleatoria en x
    posicion_y_carga = screen_height - 40  # Suelo (posición fija en y)
    cargas_suelo3.append((posicion_x_carga, posicion_y_carga))

# Generar posiciones aleatorias y movimiento de las cargas dentro de la nube
cantidad_cargas_nube = 10  # Número de cargas positivas y negativas dentro de la nube
cargas_en_nube3 = []

for _ in range(cantidad_cargas_nube):
    # Posiciones relativas a la nube
    posicion_x_carga = random.randint(0, 153 - 20)  # Dentro del área de la nube
    posicion_y_carga = random.randint(0, 82 - 20)
    velocidad_x_carga = random.choice([-2.5, 2.5]) * random.uniform(0.1, 0.3)  # Movimiento aleatorio en x
    velocidad_y_carga = random.choice([-2.5, 2.5]) * random.uniform(0.1, 0.3)  # Movimiento aleatorio en y
    # Elegir aleatoriamente si la carga es positiva o negativa
    tipo_carga = random.choice([carga_positiva_img, carga_negativa_img])
    cargas_en_nube3.append([tipo_carga, posicion_x_carga, posicion_y_carga, velocidad_x_carga, velocidad_y_carga])


def escena_simulador():
    global woodstock_movimiento2, woodstock_x, woodstock_contador, woodstock_animacion, woodstock_hablando2, boton_interrogacion_activo
    # Variables iniciales para el diálogo
    indice_texto = 0
    tiempo_inicio_texto = pygame.time.get_ticks()  # Guardar el tiempo en que comenzó a mostrar el primer texto

    def renderizar_texto(texto, posicion):
        fuente = pygame.font.Font('imagenes/PixelifySans-SemiBold.ttf', 20)  # Usa la fuente que prefieras
        lineas = texto.split('\n')  # Divide el texto en líneas
        for i, linea in enumerate(lineas):
            superficie_texto = fuente.render(linea, True, (0, 0, 0))  # Renderiza cada línea en negro
            # Ajusta la posición en Y para cada línea
            screen.blit(superficie_texto, (posicion[0], posicion[1] + i * 25))  # 25 píxeles de espacio entre líneas

    # Posiciones iniciales y otras variables de la escena
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

        # Actualizar las cargas en el suelo y la nube
        for carga in cargas_suelo3:
            screen.blit(carga_positiva_img, carga)

        for carga in cargas_en_nube3:
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

        # Movimiento de la nube
        posicion_x_nube += velocidad_nube * direccion_nube
        if posicion_x_nube <= 0 or posicion_x_nube >= screen_width - 153:
            direccion_nube *= -1

        # Movimiento de Snoopy
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

        # Botón de interrogación
        screen.blit(imagen_rayo_gris, rayo_pos)
        mouse_pos = pygame.mouse.get_pos()

        boton_separador_rect = pygame.Rect(boton_separador_pos, (60, 60))
        if boton_separador_rect.collidepoint(mouse_pos):
            screen.blit(imagen_separador_hover, boton_separador_pos)
        else:
            screen.blit(imagen_separador_normal, boton_separador_pos)

        # Funcionalidad del botón de interrogación
        boton_interrogacion_rect = pygame.Rect(boton_interrogacion_pos, (40, 40))
        if boton_interrogacion_activo:
            if boton_interrogacion_rect.collidepoint(mouse_pos):
                screen.blit(interrogacion_hover, boton_interrogacion_pos)
            else:
                screen.blit(interrogacion, boton_interrogacion_pos)
        else:
            screen.blit(interrogacion_gris, boton_interrogacion_pos)

        # Movimiento de Woodstock
        if woodstock_movimiento2:
            woodstock_x += 0.3  # Velocidad de Woodstock
            woodstock_contador += 0.27
            woodstock_animacion = (woodstock_animacion + 1) % len(woodstock_caminando)
            screen.blit(woodstock_caminando[woodstock_animacion], (woodstock_x, screen_height - 70))

            if woodstock_contador >= 120:  # Después de 4 segundos (60 fps * 4)
                woodstock_movimiento2 = False
                woodstock_camina_sound.stop()  # Detener el sonido de caminata de Woodstock
                woodstock_hablando2 = True

            # Reproducir el sonido de Woodstock caminando
            if not woodstock_camina_sound.get_num_channels():
                woodstock_camina_sound.play()

        # Si Woodstock ya está en posición y debe hablar
        if woodstock_hablando2:
            woodstock_camina_sound.stop()  # Detener el sonido de caminata de Woodstock
            # Renderizar Woodstock estático mientras habla
            screen.blit(woodstock_estatico_1, (woodstock_x, screen_height - 70))

            # Posición del globo de texto con relación a Woodstock
            globo_x = woodstock_x + 0  # Ajusta la posición en X
            globo_y = screen_height - 250 # Ajusta la posición en Y
            screen.blit(globo_imagen, (globo_x, globo_y))  # Mostrar el globo

            # Control del diálogo
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - tiempo_inicio_texto >= dialogos[indice_texto]["duracion"]:
                indice_texto += 1
                tiempo_inicio_texto = tiempo_actual

            if indice_texto < len(dialogos):
                texto_actual = dialogos[indice_texto]["texto"]
                renderizar_texto(texto_actual, (globo_x+80, globo_y +50))  # Mostrar texto dentro del globo

                # Reproducir el sonido de Woodstock hablando
                if not woodstock_habla_sound.get_num_channels():
                    woodstock_habla_sound.play()

            if indice_texto >= len(dialogos):
                woodstock_hablando2 = False  # Termina el diálogo

        # Asegurar que Woodstock siga visible una vez termine el diálogo
        if not woodstock_movimiento2 and not woodstock_hablando2:
            screen.blit(woodstock_estatico_1, (woodstock_x, screen_height - 70))

        # Procesar eventos de Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and boton_interrogacion_rect.collidepoint(mouse_pos):
                if boton_interrogacion_activo:
                    boton_interrogacion_activo = False
                    woodstock_movimiento2 = True  # Activar el movimiento de Woodstock
                    # Verificar si se hace clic en el botón separador
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_separador_rect.collidepoint(mouse_pos):
                    woodstock_camina_sound.stop()  # Detener el sonido de caminata de Woodstock
                    woodstock_habla_sound.stop()  # Detener el sonido de habla de Woodstock
                    return escena_separador()  # Cambia a la nueva escena

        pygame.display.flip()

"----------------------------------------------------------------------------------------------------------------------"
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
"----------------------------------------------------------------------------------------------------------------------"
# Cargando imágenes
fondo_1 = pygame.image.load('imagenes/Fondo_1.png')
fondo_1 = pygame.transform.scale(fondo_1, (480, 360))


nube2 = pygame.image.load('imagenes/Nube1.png')
nube2 = pygame.transform.scale(nube2, (400, 330))

carga_positiva_img2 = pygame.image.load('imagenes/carga_positiva2.png')
carga_positiva_img2 = pygame.transform.scale(carga_positiva_img2, (120, 120))  # Tamaño de la carga positiva
carga_negativa_img2 = pygame.image.load('imagenes/carga_negativa2.png')
carga_negativa_img2 = pygame.transform.scale(carga_negativa_img2, (120, 120))  # Tamaño de la carga negativa

cantidad_cargas_nube2 = 10  # Número de cargas positivas y negativas dentro de la nube
cargas_en_nube2 = []

# Configuración de cargas en la nube con velocidad inicial
for _ in range(cantidad_cargas_nube2):
    posicion_x_carga2 = random.randint(0, 400 - 0)  # Dentro del área de la nube
    posicion_y_carga2 = random.randint(0, 330 - 120)
    velocidad_x_carga2 = 0
    tipo_carga2 = random.choice([carga_positiva_img2, carga_negativa_img2])

    # Dirección inicial en y según el tipo de carga
    velocidad_y_carga2 = -0.04 if tipo_carga2 == carga_positiva_img2 else 0.03
    cargas_en_nube2.append([tipo_carga2, posicion_x_carga2, posicion_y_carga2, velocidad_x_carga2, velocidad_y_carga2])


def manejar_movimiento_cargas():
    """ Actualiza el movimiento de las cargas en la nube """
    for carga in cargas_en_nube2:
        tipo_carga, carga_x, carga_y, velocidad_x, velocidad_y = carga

        # Movimiento de la carga
        carga_x += velocidad_x
        carga_y += velocidad_y

        # Mantener las cargas dentro de los límites de la ventana de 480x360
        if carga_x < 0:
            carga_x = 0  # Limitar en el borde izquierdo
            velocidad_x = abs(velocidad_x)  # Cambiar dirección a la derecha
        elif carga_x > screen_width - 120:  # 120 es el ancho de la carga
            carga_x = screen_width - 120  # Limitar en el borde derecho
            velocidad_x = -abs(velocidad_x)  # Cambiar dirección a la izquierda

        # Rebotar en el borde superior e inferior
        if carga_y < 0:
            carga_y = 0
            velocidad_y = -velocidad_y * 0.799999  # Cambiar dirección y reducir la velocidad
        elif carga_y > screen_height - 120:  # 120 es la altura de la carga
            carga_y = screen_height - 120
            velocidad_y = -velocidad_y  * 0.79999  # Cambiar dirección y reducir la velocidad

        # Impulso constante hacia arriba para cargas positivas
        if tipo_carga == carga_positiva_img2:
            velocidad_y -= 0.005  # Aumentar la velocidad hacia arriba
        else:
            velocidad_y += 0.005  # Aumentar la velocidad hacia abajo

        # Colisión y repulsión entre cargas
        for otra_carga in cargas_en_nube2:
            if carga != otra_carga:  # Verificar que no es la misma carga
                tipo_otra_carga, otra_x, otra_y, otra_vel_x, otra_vel_y = otra_carga
                distancia = ((carga_x - otra_x) ** 2 + (carga_y - otra_y) ** 2) ** 0.5

                # Verificar colisión s están suficientemente cerca
                if distancia < 120:  # Ajusta este valor según el tamaño de las cargas
                    if tipo_carga != tipo_otra_carga:  # Solo reaccionan si son opuestas
                        # Repulsión
                        if tipo_carga == carga_positiva_img2:
                            velocidad_x, velocidad_y = 0.5, -1  # Repulsión hacia arriba y a la izquierda
                            otra_vel_x, otra_vel_y = -0.5, 1  # Repulsión hacia abajo y a la derecha
                        else:
                            velocidad_x, velocidad_y = -0.5, 1  # Repulsión hacia abajo y a la derecha
                            otra_vel_x, otra_vel_y = 0.5, -1  # Repulsión hacia arriba y a la izquierda

                        # Actualizar velocidades de ambas cargas tras la colisión
                        otra_carga[3] = otra_vel_x
                        otra_carga[4] = otra_vel_y

        # Actualizar la carga en la lista
        carga[1] = carga_x
        carga[2] = carga_y
        carga[3] = velocidad_x
        carga[4] = velocidad_y

        # Dibujar la carga en su nueva posición
        screen.blit(tipo_carga, (carga_x + 35, carga_y + 10))  # Ajuste dentro de la nube


fuente_pixel = pygame.font.Font('imagenes/PixelifySans-SemiBold.ttf',20)  # Cambia esto por tu fuente de pixel si la tienes
texto_surface = fuente_pixel.render("Presione esc para saltar", True, (0, 0, 0))
texto_rect = texto_surface.get_rect(topright=(268 - 10, 10))  # Posición arriba a la derecha

# Cargar imágenes del botón y redimensionarlas
boton_grande_imagen_normal = pygame.image.load('imagenes/interrogacion.png')
boton_grande_imagen_normal = pygame.transform.scale(boton_grande_imagen_normal, (40, 40))

boton_grande_imagen_hover = pygame.image.load('imagenes/interrogacion_hover.png')
boton_grande_imagen_hover = pygame.transform.scale(boton_grande_imagen_hover, (40, 40))

boton_grande_imagen_presionado = pygame.image.load('imagenes/interrogacion_gris.png')
boton_grande_imagen_presionado = pygame.transform.scale(boton_grande_imagen_presionado, (40, 40))

# Variables del botón
boton_grande_rect = pygame.Rect(screen_width - 50, 10, 40, 40)  # Cambia la posición y tamaño según sea necesario
boton_grande_presionado = False

dialogos2 = [
    {"texto": "¡Hola, aquí abajo!", "duracion": 2000},  # 2 segundos
    {"texto": "QUE?, no sabes lo \n que ocurre?", "duracion": 3000},  # 3 segundos
    {"texto": "Mira, en la nube \nhay dos tipos de \npartículas: ", "duracion": 3000},  # 3 segundos
    {"texto": "el graupel, que \nes como bolitas\n de hielo,\n.", "duracion": 3000},  # 3 segundos
    {"texto": "y los copos\n de nieve", "duracion": 2000},  # 3 segundos
    {"texto": "Cuando el graupel\n y los copos de\n nieve chocan,", "duracion": 2000},  # 3 segundos
    {"texto": "el graupel se\n queda con cargas \npositivas", "duracion": 2000},  # 3 segundos
    {"texto": "y los copos \nde nieve \n", "duracion": 2000},  # 3 segundos
    {"texto": "se quedan\n con cargas \nnegativas", "duracion": 2000},  # 3 segundos
    {"texto": "y van a la \nparte baja de\n la nube.", "duracion": 2000},  # 3 segundos
    {"texto": "así, la nube \n se carga:", "duracion": 2000},  # 3 segundos
    {"texto": "la parte de arriba \ncon cargas \npositivas ", "duracion": 2000},  # 3 segundos
    {"texto": "y la de abajo\n con negativas.", "duracion": 2000},  # 3 segundos
    {"texto": " ¡Y cuando se \nacumula suficiente \ncarga,", "duracion": 2000},  # 3 segundos
    {"texto": " se puede formar \nun rayo!", "duracion": 2000},  # 3 segundos
]

# Variables para controlar el estado de Woodstock
woodstock_x2 = -120  # Posición inicial fuera de la pantalla
woodstock_hablando2 = False
woodstock_dialogo_index2 = 0
woodstock_dialogo_tiempo2 = 0
woodstock_movimiento2 = False

globo_texto = pygame.image.load('imagenes/globo_texto.png')
globo_texto = pygame.transform.scale(globo_texto, (300, 150))  # Ajusta el tamaño según sea necesario

woodstock_estatico_2 = pygame.image.load('imagenes/Sprites_woodstock/woodstock_estatico_2.png')
woodstock_estatico_2 = pygame.transform.scale(woodstock_estatico_2, (120, 120))  # Ajusta el tamaño de Woodstock

def renderizar_texto2(texto2, posicion2):
    fuente = pygame.font.Font('imagenes/PixelifySans-SemiBold.ttf', 14)
    lineas = texto2.split('\n')
    for i, linea in enumerate(lineas):
        superficie_texto = fuente.render(linea, True, (0, 0, 0))
        screen.blit(superficie_texto, (posicion2[0], posicion2[1] + i * 25))

def dibujar_boton():
    mouse_pos = pygame.mouse.get_pos()
    if boton_grande_rect.collidepoint(mouse_pos):
        screen.blit(boton_grande_imagen_hover, boton_grande_rect.topleft)
    else:
        screen.blit(boton_grande_imagen_normal, boton_grande_rect.topleft)

def escena_separador(woodstock_dialogo_index2=0, woodstock_x2=-50):
    global woodstock_movimiento2, woodstock_hablando2, woodstock_dialogo_tiempo2

    # Asegúrate de que el movimiento de Woodstock esté desactivado al entrar en la escena separador
    woodstock_movimiento2 = False
    woodstock_hablando2 = False
    woodstock_x2 = -120  # Posición inicial fuera de la pantalla
    woodstock_regresando = False  # Nueva variable para controlar el regreso de Woodstock

    run = True

    while run:
        screen.blit(fondo_1, (0, 0))
        screen.blit(nube2, (35, 10))
        screen.blit(texto_surface, texto_rect)

        # Dibujar el botón
        dibujar_boton()

        # Llamar a la función que maneja el movimiento de las cargas
        manejar_movimiento_cargas()

        # Movimiento de Woodstock
        if woodstock_movimiento2:
            woodstock_x2 += 0.5
            screen.blit(woodstock_estatico_2, (woodstock_x2, screen_height // 2 - 60))  # Centrado verticalmente

            if woodstock_x2 >= 25:
                woodstock_movimiento2 = False
                woodstock_hablando2 = True

        # Si Woodstock ya está en posición y debe hablar
        if woodstock_hablando2:
            screen.blit(woodstock_estatico_2, (woodstock_x2, screen_height // 2 - 60))

            # Posición del globo de texto con relación a Woodstock
            globo_x = woodstock_x2 + 10
            globo_y = screen_height // 2 - 200
            screen.blit(globo_texto, (globo_x, globo_y))

            # Control del diálogo
            tiempo_actual2 = pygame.time.get_ticks()
            if tiempo_actual2 - woodstock_dialogo_tiempo2 >= dialogos2[woodstock_dialogo_index2]["duracion"]:
                woodstock_dialogo_index2 += 1
                woodstock_dialogo_tiempo2 = tiempo_actual2

            if woodstock_dialogo_index2 < len(dialogos2):
                texto_actual = dialogos2[woodstock_dialogo_index2]["texto"]
                renderizar_texto2(texto_actual, (globo_x + 80, globo_y + 37))

            else:
                woodstock_hablando2 = False  # Terminar de hablar
                woodstock_dialogo_index2 = 0  # Reiniciar el índice de diálogo
                woodstock_regresando = True  # Comienza el regreso

        # Movimiento de regreso de Woodstock
        if woodstock_regresando:
            woodstock_x2 -= 0.5  # Deslizar hacia la izquierda
            screen.blit(woodstock_estatico_2, (woodstock_x2, screen_height // 2 - 60))  # Renderizar mientras se desliza
            if woodstock_x2 <= -120:  # Cuando regrese a la posición inicial
                woodstock_x2 = -120  # Asegurarse de que no se pase de la posición
                woodstock_regresando = False  # Detener el regreso

        # Procesar eventos de Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and boton_interrogacion_pos[0] < event.pos[0] < boton_interrogacion_pos[0] + 30 and boton_interrogacion_pos[1] < event.pos[1] < boton_interrogacion_pos[1] + 30:
                woodstock_movimiento2 = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Presiona ESC para volver
                    escena_3()

        pygame.display.flip()

"----------------------------------------------------------------------------------------------------------------------"
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
"----------------------------------------------------------------------------------------------------------------------"

def escena_3():
    global woodstock_movimiento2, woodstock_x, woodstock_contador, woodstock_animacion, woodstock_hablando2, boton_interrogacion_activo

    snoopy_avisado = pygame.image.load('imagenes/Sprites_snoopy/Snoopy_avisado.png')
    snoopy_aturdido = pygame.image.load('imagenes/Sprites_snoopy/Snoopy_aturdido.png')
    snoopy_electrocutado = pygame.image.load('imagenes/Sprites_snoopy/Snoopy_electrocutado.png')

    snoopy_avisado = pygame.transform.scale(snoopy_avisado, (70, 110))
    snoopy_aturdido = pygame.transform.scale(snoopy_aturdido, (80, 120))
    snoopy_electrocutado = pygame.transform.scale(snoopy_electrocutado, (120, 160))

    # Variables de la nube y Snoopy
    posicion_x_nube2 = random.randint(0, screen_width - 153)
    posicion_y_nube2 = 50
    posicion_x_snoopy2 = random.randint(0, screen_width - 80)
    posicion_y_snoopy2 = screen_height - 120  # Ajustado para que Snoopy esté en el suelo
    velocidad_nube2 = 0.2
    velocidad_snoopy2 = 0.5
    direccion_nube2 = 1
    direccion_snoopy2 = 1
    indice_snoopy2 = 0
    contador_animacion_snoopy2 = 0
    velocidad_animacion_snoopy2 = 50
    mirando_derecha2 = True
    boton_rayo_presionado2 = False
    mostrar_rayo = False
    animacion_rayo_activa = False
    contador_animacion_rayo = 0
    estado_snoopy = 'caminando'
    tiempo_aturdido = 0

    # Cargas en el suelo y en la nube
    cantidad_cargas_suelo2 = 6
    cargas_suelo = [[random.randint(0, screen_width - 20), screen_height - 40, carga_positiva_img] for _ in range(cantidad_cargas_suelo2)]
    area_cargas_positivas = (posicion_x_nube2, posicion_y_nube2, 153, 40)
    area_cargas_negativas = (posicion_x_nube2, posicion_y_nube2 + 45, 120, 40)
    cargas_en_nube3 = []

    # Partículas en la nube
    for _ in range(6):
        carga_x = random.randint(0, area_cargas_positivas[2] - 20)
        carga_y = random.randint(0, area_cargas_positivas[3] - 20)
        direccion = random.choice([-1, 1])
        cargas_en_nube3.append([carga_positiva_img, carga_x, carga_y, direccion])

    for _ in range(4):
        carga_x = random.randint(0, area_cargas_negativas[2] - 20)
        carga_y = random.randint(0, area_cargas_negativas[3] - 20) + 35
        direccion = random.choice([-1, 1])
        cargas_en_nube3.append([carga_negativa_img, carga_x, carga_y, direccion])

    def pantalla_principal():
        screen.blit(fondo2, (0, 0))
        screen.blit(casita_snopy, (340, 178))
        screen.blit(nube1, (posicion_x_nube2, posicion_y_nube2))

        # Dibujar cargas en el suelo
        for carga in cargas_suelo:
            screen.blit(carga[2], (carga[0], carga[1]))

        # Dibujar cargas en la nube
        for carga in cargas_en_nube3:
            tipo_carga, carga_x, carga_y, direccion = carga
            carga_x += direccion
            if carga_x <= 0 or carga_x >= area_cargas_positivas[2] - 20:
                carga[3] *= -1
            screen.blit(tipo_carga, (posicion_x_nube2 + carga_x, posicion_y_nube2 + carga_y))
            carga[1] = carga_x

        # Mostrar animación del rayo si está activa
        if animacion_rayo_activa:
            indice_sprite = contador_animacion_rayo // 5  # Cambiar sprite cada 5 frames
            if indice_sprite < len(sprites_rayo):
                screen.blit(sprites_rayo[indice_sprite], (posicion_x_nube2 + 25, posicion_y_nube2 + 76))

    def mover_nube():
        nonlocal posicion_x_nube2, direccion_nube2
        if not boton_rayo_presionado2:
            posicion_x_nube2 += velocidad_nube2 * direccion_nube2
            if posicion_x_nube2 <= 0 or posicion_x_nube2 >= screen_width - 153:
                direccion_nube2 *= -1

    # Cargar sprites del rayo
    sprites_rayo = []
    for i in range(1, 8):
        sprite = pygame.image.load(f'imagenes/sprites_rayo/{i}.png')
        sprite = pygame.transform.scale(sprite, (100, 210))  # Aumentado el alto a 280
        sprites_rayo.append(sprite)

    def mover_cargas_en_tren():
        for i in range(len(cargas_suelo) - 1, -1, -1):
            carga_x, carga_y, tipo_carga = cargas_suelo[i]

            if carga_x < posicion_x_nube2 + 76:
                carga_x += 1
            elif carga_x > posicion_x_nube2 + 76:
                carga_x -= 1

            if abs(carga_x - (posicion_x_nube2 + 76)) < 5:
                if carga_y > posicion_y_nube2 + 40:
                    carga_y -= 1
                else:
                    cargas_en_nube3.append([tipo_carga, carga_x - posicion_x_nube2, carga_y - posicion_y_nube2, random.choice([-1, 1])])
                    cargas_suelo.pop(i)
                    return True

            cargas_suelo[i] = [carga_x, carga_y, tipo_carga]
        return False
        # Añadir variables para el efecto de temblor
    temblor_x = 0
    temblor_y = 0
    intensidad_temblor = 5

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_rayo_rect.collidepoint(mouse_pos):
                    # Verificar si Snoopy está debajo de la nube
                    if (posicion_x_snoopy2 + 80 > posicion_x_nube2) and (posicion_x_snoopy2 < posicion_x_nube2 + 153) and (posicion_y_snoopy2 + 120 >= posicion_y_nube2):
                        boton_rayo_presionado2 = True
                        estado_snoopy = 'avisado'  # Cambiar a estado avisado
                        snoopy_avisado_sound.play()  # Reproducir el sonido de Snoopy avisado
                elif boton_separador_rect.collidepoint(mouse_pos):
                    run = False
                    escena_separador()

        mover_nube()
        pantalla_principal()

        # Dibujar Snoopy según su estado
        if estado_snoopy == 'caminando':
            posicion_x_snoopy2 += velocidad_snoopy2 * direccion_snoopy2
            if posicion_x_snoopy2 <= 0 or posicion_x_snoopy2 >= screen_width - 80:
                direccion_snoopy2 *= -1
                mirando_derecha2 = not mirando_derecha2

            contador_animacion_snoopy2 += 1
            if contador_animacion_snoopy2 >= velocidad_animacion_snoopy2:
                contador_animacion_snoopy2 = 0
                indice_snoopy2 = (indice_snoopy2 + 1) % len(snoopy_caminando)

            if mirando_derecha2:
                screen.blit(snoopy_caminando[indice_snoopy2], (posicion_x_snoopy2, posicion_y_snoopy2))
            else:
                snoopy_volteado = pygame.transform.flip(snoopy_caminando[indice_snoopy2], True, False)
                screen.blit(snoopy_volteado, (posicion_x_snoopy2, posicion_y_snoopy2))

        elif estado_snoopy == 'avisado':
            screen.blit(snoopy_avisado, (posicion_x_snoopy2, posicion_y_snoopy2))
            if mover_cargas_en_tren():
                animacion_rayo_activa = True
                contador_animacion_rayo = 0
                estado_snoopy = 'electrocutado'
                tiempo_inicio_electrocutado = pygame.time.get_ticks()
                rayo_cayendo_sound.play()  # Reproducir el sonido del rayo

        elif estado_snoopy == 'electrocutado':
            # Efecto de temblor
            tiempo_actual = pygame.time.get_ticks()
            tiempo_electrocutado = tiempo_actual - tiempo_inicio_electrocutado

            if tiempo_electrocutado < 2000:  # Duración del efecto de electrocutado (2 segundos)
                # Generar temblor aleatorio
                temblor_x = random.randint(-intensidad_temblor, intensidad_temblor)
                temblor_y = random.randint(-intensidad_temblor, intensidad_temblor)

                # Aplicar el temblor a la posición de Snoopy
                pos_x_temblor = posicion_x_snoopy2 + temblor_x
                pos_y_temblor = posicion_y_snoopy2 + temblor_y

                # Dibujar Snoopy electrocutado con efecto de temblor
                screen.blit(snoopy_electrocutado, (pos_x_temblor, pos_y_temblor))

                # Efecto adicional: cambiar rápidamente entre normal y volteado
                if tiempo_electrocutado % 100 < 50:  # Cambiar cada 50 ms
                    screen.blit(snoopy_electrocutado, (pos_x_temblor, pos_y_temblor))
                else:
                    snoopy_electrocutado_volteado = pygame.transform.flip(snoopy_electrocutado, True, False)
                    screen.blit(snoopy_electrocutado_volteado, (pos_x_temblor, pos_y_temblor))
            else:
                estado_snoopy = 'aturdido'
                tiempo_aturdido = pygame.time.get_ticks()
                rayo_cayendo_sound.stop()  # Detener el sonido del rayo
                asado_sound.play()  # Reproducir el sonido de asado

        elif estado_snoopy == 'aturdido':
            screen.blit(snoopy_aturdido, (posicion_x_snoopy2, posicion_y_snoopy2))
            if pygame.time.get_ticks() - tiempo_aturdido >= 1000:
                estado_snoopy = 'caminando'
                boton_rayo_presionado2 = False
                asado_sound.stop()  # Detener el sonido de asado

        mouse_pos = pygame.mouse.get_pos()
        boton_rayo_rect = pygame.Rect(rayo_pos, (60, 60))
        boton_separador_rect = pygame.Rect(boton_separador_pos, (60, 60))

        screen.blit(imagen_rayo_hover if boton_rayo_rect.collidepoint(mouse_pos) else imagen_rayo, rayo_pos)
        screen.blit(imagen_separador_hover if boton_separador_rect.collidepoint(mouse_pos) else imagen_separador_normal, boton_separador_pos)

        if animacion_rayo_activa:
            tiempo_actual = pygame.time.get_ticks()  # Obtener el tiempo actual
            if not hasattr(escena_3, 'tiempo_inicio_rayo'):
                escena_3.tiempo_inicio_rayo = tiempo_actual # Guardar el tiempo de inicio

            # Calcular el tiempo transcurrido
            tiempo_transcurrido = tiempo_actual - escena_3.tiempo_inicio_rayo

            # Si no han pasado 2 segundos, continuar la animación
            if tiempo_transcurrido < 2000:  # 2000 ms = 2 segundos
                contador_animacion_rayo += 1
                indice_sprite = (contador_animacion_rayo // 5) % len(sprites_rayo)
                screen.blit(sprites_rayo[indice_sprite], (posicion_x_nube2 + 25, posicion_y_nube2 + 76))
            else:
                # Después de 2 segundos, resetear todo
                animacion_rayo_activa = False
                boton_rayo_presionado2 = False
                delattr(escena_3, 'tiempo_inicio_rayo')  # Limpiar el tiempo guardado
                # Reiniciar las cargas en el suelo
                cargas_suelo = [[random.randint(0, screen_width - 20), screen_height - 40, carga_positiva_img]
                                for _ in range(cantidad_cargas_suelo2)]


        pygame.display.flip()



"----------------------------------------------------------------------------------------------------------------------"
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
"----------------------------------------------------------------------------------------------------------------------"

if __name__ == '__main__':
    menu_principal()
    pygame.quit()
