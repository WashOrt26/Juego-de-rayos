import random

import pygame

pygame.init()
pygame.font.init()

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
                woodstock_hablando2 = True

        # Si Woodstock ya está en posición y debe hablar
        if woodstock_hablando2:
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
texto_rect = texto_surface.get_rect(topright=(480 - 10, 10))  # Posición arriba a la derecha

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
    {"texto": "aña", "duracion": 2000},  # 4 segundos
    {"texto": "Mira bien lo \nque pasa\n en el \n cielo", "duracion": 3000},  # 3 segundos
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
    fuente = pygame.font.Font('imagenes/PixelifySans-SemiBold.ttf', 20)
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
    global woodstock_visible, woodstock_deslizandose, dialogo_tiempo, boton_grande_presionado, woodstock_movimiento2, woodstock_hablando2, woodstock_x, woodstock_dialogo_tiempo2
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
            screen.blit(woodstock_estatico_2, (woodstock_x2, screen_height // 2 -60))

            # Posición del globo de texto con relación a Woodstock
            globo_x = woodstock_x2 + 10
            globo_y = screen_height // 2 -200
            screen.blit(globo_texto, (globo_x, globo_y))

            # Control del diálogo
            tiempo_actual2 = pygame.time.get_ticks()
            if tiempo_actual2 - woodstock_dialogo_tiempo2 >= dialogos2[woodstock_dialogo_index2]["duracion"]:
                woodstock_dialogo_index2 += 1
                woodstock_dialogo_tiempo2 = tiempo_actual2

            if woodstock_dialogo_index2 < len(dialogos2):
                texto_actual = dialogos2[woodstock_dialogo_index2]["texto"]
                renderizar_texto2(texto_actual, (globo_x + 80, globo_y + 50))

            else:
                woodstock_dialogo_index2 += 1
                if woodstock_dialogo_index2 >= len(dialogos2):
                    woodstock_hablando2 = False  # Terminar de hablar
                    woodstock_dialogo_index2 = 0  # Reiniciar el índice de diálogo
                    woodstock_x2 = -120  # Volver a la posición inicial
                else:
                    woodstock_dialogo_tiempo2 = tiempo_actual2  # Reiniciar el tiempo del nuevo diálogo

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
    # Posiciones iniciales y otras variables de la escena
    posicion_x_nube2 = random.randint(0, screen_width - 153)
    posicion_y_nube2 = 50
    posicion_x_snoopy2 = random.randint(0, screen_width - 150)
    posicion_y_snoopy2 = 220
    velocidad_nube2 = 0.2
    velocidad_snoopy2 = 0.5
    direccion_nube2 = 1
    direccion_snoopy2 = 1
    indice_snoopy2 = 0
    contador_animacion_snoopy2 = 0
    velocidad_animacion_snoopy2 = 50
    mirando_derecha2 = True
    boton_rayo_presionado2 = False

    # Inicializar cargas en la nube
    cantidad_cargas_suelo2 = 6
    cargas_suelo3 = [[random.randint(0, screen_width - 20), screen_height - 40, carga_positiva_img] for _ in range(cantidad_cargas_suelo2)]
    # Áreas para las cargas en la nube
    area_cargas_positivas = (posicion_x_nube2, posicion_y_nube2, 153, 40)  # Parte superior de la nube
    area_cargas_negativas = (posicion_x_nube2, posicion_y_nube2 + 45, 120, 40)  # Parte inferior de la nube (ajustado)


    # Generar posiciones y movimiento de cargas en la nube
    cantidad_cargas_nube = 10
    cargas_en_nube3 = []

    # Añadir partículas positivas a la parte superior y negativas a la inferior
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

    def mover_cargas_en_tren(posicion_x_nube2, posicion_y_nube2):
        """Inicia el intercambio de cargas desde el suelo a la nube."""
        global cargas_suelo3, cargas_en_nube3

        for i, carga_suelo in enumerate(cargas_suelo3):
            carga_x, carga_y = carga_suelo
            while carga_x != posicion_x_nube2:
                carga_x += 1 if carga_x < posicion_x_nube2 else -1  # Movimiento en x hacia la nube
                pantalla_principal(posicion_x_nube2)
                pygame.display.flip()

            while carga_y > posicion_y_nube2 + i * 10:
                carga_y -= 1  # Movimiento en y hacia la nube
                pantalla_principal(posicion_x_nube2)
                pygame.display.flip()
                pygame.time.delay(10)

            # Al llegar a la nube, intercambiar con una carga en la nube
            if i < len(cargas_en_nube3):
                cargas_en_nube3[i][1], cargas_en_nube3[i][2] = carga_x - posicion_x_nube2, carga_y - posicion_y_nube2
                cargas_suelo3[i] = [random.randint(0, screen_width - 20), screen_height - 40, tipo_carga]

    def pantalla_principal(posicion_x_nube2):
        """Dibuja fondo, nube, botón y cargas en pantalla."""
        screen.blit(fondo2, (0, 0))
        screen.blit(nube1, (posicion_x_nube2, posicion_y_nube2))

        # Dibujar botón de rayo
        mouse_pos = pygame.mouse.get_pos()
        boton_rayo_rect = pygame.Rect(rayo_pos, (60, 60))
        screen.blit(imagen_rayo_hover if boton_rayo_rect.collidepoint(mouse_pos) else imagen_rayo, rayo_pos)

        # Dibujar cargas en el suelo
        for carga in cargas_suelo3:
            screen.blit(carga[2], (carga[0], carga[1]))

        # Dibujar cargas en la nube
        for carga in cargas_en_nube3:
            tipo_carga, carga_x, carga_y, direccion = carga

            # Mover la carga dentro de los límites de la nube
            carga_x += direccion  # Movimiento horizontal
            if carga_x <= 0 or carga_x >= area_cargas_positivas[2] - 20:
                carga[3] *= -1  # Invertir dirección

            # Dibujar la carga en la posición actualizada
            screen.blit(tipo_carga, (posicion_x_nube2 + carga_x, posicion_y_nube2 + carga_y))
            carga[1] = carga_x  # Actualizar posición

    def mover_nube(posicion_x_nube2, direccion_nube2):
        """Movimiento de la nube si el botón de rayo no se ha presionado."""

        posicion_x_nube2 += velocidad_nube2 * direccion_nube2
        if posicion_x_nube2 <= 0 or posicion_x_nube2 >= screen_width - 153:
            direccion_nube2 *= -1  # Cambia la dirección

    run = True
    while run:
        screen.blit(fondo2, (0, 0))
        screen.blit(casita_snopy, (340, 178))
        screen.blit(nube1, (posicion_x_nube2, posicion_y_nube2))


        pantalla_principal(posicion_x_nube2)

        if not boton_rayo_presionado2:
            mover_nube(posicion_x_nube2, direccion_nube2)  # Movimiento de la nube mientras no se presione el botón de rayo


        # Movimiento de Snoopy
        posicion_x_snoopy2 += velocidad_snoopy2 * direccion_snoopy2
        if posicion_x_snoopy2 <= 0 or posicion_x_snoopy2 >= screen_width - 90:
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
            # Botón de interrogación
        screen.blit(imagen_rayo, rayo_pos)
        mouse_pos = pygame.mouse.get_pos()
        boton_rayo_rect = pygame.Rect(rayo_pos, (60, 60))
        if boton_rayo_rect.collidepoint(mouse_pos):
            screen.blit(imagen_rayo_hover, rayo_pos)
        else:
            screen.blit(imagen_rayo, rayo_pos)
        boton_separador_rect = pygame.Rect(boton_separador_pos, (60, 60))
        if boton_separador_rect.collidepoint(mouse_pos):
            screen.blit(imagen_separador_hover, boton_separador_pos)
        else:
            screen.blit(imagen_separador_normal, boton_separador_pos)
            # Procesar eventos de Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_separador_rect.collidepoint(mouse_pos):
                    return escena_separador()  # Cambia a la nueva escena
                elif boton_rayo_rect.collidepoint(mouse_pos):
                    boton_rayo_presionado2 = True
                    mover_cargas_en_tren(posicion_x_nube2, posicion_y_nube2)
        pygame.display.flip()

"----------------------------------------------------------------------------------------------------------------------"
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
"----------------------------------------------------------------------------------------------------------------------"

if __name__ == '__main__':
    escena_simulador()
    pygame.quit()
