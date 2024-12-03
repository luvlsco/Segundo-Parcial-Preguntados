# src/ventana_jugar.py
# Módulo que controla la ventana principal del botón "Jugar"

import pygame
import random
import src.game.config as config

from src.game.questions import *
from src.game.functions import *

from src.assets.images import *
from src.assets.sounds import *

def ventana_jugar(variable_ventana: pygame.Surface) -> str:
    '''
    Función para mostrar en pantalla el juego.

    ¿Qué hace?:
        - Gestiona el juego, controla las preguntas y respuestas, verifica las respuestas correctas y actualiza la puntuación y resta vidas en caso de error.
        - Detecta los clicks y ejecuta los eventos correspondientes.
        - Muestra un mensaje indicando el final del juego
        - Pide el ingreso del nombre del jugador para guardarlo en el ranking

    ¿Qué recibe?:
        - variable_ventana: Donde se renderiza el juego 

    ¿Qué retorna?:
        - ventana_completada: Indica que el juego terminó correctamente.
    '''

    # Cambiar el título de la ventana, establecer la fuente y reproducir la música
    pygame.display.set_caption("Preguntados: Jugando")
    random.shuffle(diccionario_preguntas)
    reproducir_musica("assets/sounds/music/ventana_jugar.mp3", 1, -1, True)

    # Importación de las configuraciones
    global puntuacion_correcta, vidas
    puntuacion = 0 # Puntuación (Acumulador)
    vidas_jugando = config.vidas

    pregunta_actual = 0 
    mostrando_respuesta = False
    color_respuesta = (255, 255, 0)
    fuente = cargar_fuente_personalizada("assets/fonts/fuente_preguntados.otf", 26)

    while True:
        configurar_fps(FPS)
        variable_ventana.blit(pantalla_jugar, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_juego()

            if evento.type == pygame.MOUSEBUTTONDOWN and not mostrando_respuesta:
                mouse_pos = pygame.mouse.get_pos()
                for i, opcion_rect in enumerate(opciones_rects):
                    if opcion_rect.collidepoint(mouse_pos):

                        if i == diccionario_preguntas[pregunta_actual]["respuesta_correcta"]:
                            puntuacion += config.puntuacion_correcta
                            color_respuesta = ((0, 255, 0))
                            efecto_sonido_correcto.play()
                        else:
                            vidas_jugando -= 1
                            color_respuesta = ((255, 0, 0))
                            efecto_sonido_incorrecto.play()
                        mostrando_respuesta = True
                        break

        # Mostrar pregunta
        pregunta_texto = fuente.render(diccionario_preguntas[pregunta_actual]["pregunta"], True, ((0, 0, 0)))
        variable_ventana.blit(pregunta_texto, (50, 45))

        # Mostrar opciones
        opciones_rects = []
        for i, opcion in enumerate(diccionario_preguntas[pregunta_actual]["opciones"]):
            opcion_texto = fuente.render(opcion, True, (0, 0, 0))
            opcion_rect = opcion_texto.get_rect(topleft=(50, 143 + i * 50))
            opciones_rects.append(opcion_rect)
            variable_ventana.blit(opcion_texto, opcion_rect.topleft)

        # Mostrar respuesta si está en modo de respuesta
        if mostrando_respuesta:
            pygame.draw.rect(variable_ventana, color_respuesta, opciones_rects[diccionario_preguntas[pregunta_actual]["respuesta_correcta"]], 3,)
            pygame.time.wait(2000) # Esperar 2 segundos
            mostrando_respuesta = False
            color_respuesta = (255, 255, 0)
            pregunta_actual += 1
            if pregunta_actual >= len(diccionario_preguntas):
                break

        # Mostrar puntuación y vidas
        puntuacion_texto = fuente.render(f"Puntuación: {puntuacion}", True, (255, 255, 255))
        vidas_texto = fuente.render(f"Vidas: {vidas_jugando}", True, (235, 66, 112))
        variable_ventana.blit(puntuacion_texto, (50, 495))
        variable_ventana.blit(vidas_texto, (630, 500))

        # Revisar si se acabaron las vidas
        if vidas_jugando == 0:
            break

        actualizar_pantalla()

    # Pantalla final (Game Over)
    variable_ventana.fill((0, 0, 0))
    mensaje_final = fuente.render("¡Fin del juego!", True, (255, 255, 255))
    puntuacion_final = fuente.render(f"Puntuación final: {puntuacion}", True, (255, 255, 255))
    variable_ventana.blit(mensaje_final, (300, 250))
    variable_ventana.blit(puntuacion_final, (275, 300))
    actualizar_pantalla()
    pygame.time.wait(3000)

    nombre = solicitar_nombre(variable_ventana, fuente)
    guardar_clasificacion(nombre, puntuacion)
    reproducir_musica("assets/sounds/music/menu_principal.mp3", 1, -1, True)

    # Cuando toda la ventana termina de ejecutarse retorna esta cadena a la variable 
    # "estado_ventana_jugar" usada en el menú principal "src/menu_principal.py" .

    # Esto es útil para evitar el uso de clases o una lista de pantallas, ya que se maneja
    # de manera más simple todas las ventanas del juego.
    return "ventana_completada"