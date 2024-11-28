import pygame
import json
import random
import sys

from src.assets.images import *
from src.assets.sounds import *

from src.game.questions import *
from src.game.functions import *

puntuacion = 0
puntuacion_correcta = 1
vidas = 3

def ventana_jugar():

    global puntuacion_correcta, vidas
    puntuacion = 0

    pygame.init()
    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Jugar")

    random.shuffle(diccionario_preguntas)

    fuente = pygame.font.Font(None, 36)

    pregunta_actual = 0
    mostrando_respuesta = False
    color_respuesta = (255, 255, 0)

    ventana.blit(pantalla_jugar, (0, 0)) 

    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN and not mostrando_respuesta:
            mouse_pos = pygame.mouse.get_pos()
            for i, opcion_rect in enumerate(opciones_rects):
                if opcion_rect.collidepoint(mouse_pos):

                    if i == diccionario_preguntas[pregunta_actual]["respuesta_correcta"]:
                        puntuacion += puntuacion_correcta
                        color_respuesta = ((0, 255, 0))
                            
                    else:
                        vidas -= 1
                        color_respuesta = ((255, 0, 0))
                    mostrando_respuesta = True
                    break

        # Mostrar pregunta
        pregunta_texto = fuente.render(
            diccionario_preguntas[pregunta_actual]["pregunta"], True, ((0, 0, 0))
        )
        ventana.blit(pregunta_texto, (50, 50))

        # Mostrar opciones
        opciones_rects = []
        for i, opcion in enumerate(diccionario_preguntas[pregunta_actual]["opciones"]):
            opcion_texto = fuente.render(opcion, True, (0, 0, 0))
            opcion_rect = opcion_texto.get_rect(topleft=(50, 150 + i * 50))
            opciones_rects.append(opcion_rect)
            ventana.blit(opcion_texto, opcion_rect.topleft)

        # Mostrar respuesta si está en modo de respuesta
        if mostrando_respuesta:
            pygame.draw.rect(
                ventana,
                color_respuesta,
                opciones_rects[diccionario_preguntas[pregunta_actual]["respuesta_correcta"]],
                3,
            )
            pygame.time.wait(2000)  # Esperar 2 segundos
            mostrando_respuesta = False
            color_respuesta = (0, 0, 0)
            pregunta_actual += 1
            if pregunta_actual >= len(diccionario_preguntas):
                corriendo = False

        # Mostrar puntuación y vidas
        puntuacion_texto = fuente.render(f"Puntuación: {puntuacion}", True, (255, 255, 255))
        vidas_texto = fuente.render(f"Vidas: {vidas}", True, (255, 0, 0))
        ventana.blit(puntuacion_texto, (50, 500))
        ventana.blit(vidas_texto, (650, 500))

        # Revisar si se acabaron las vidas
        if vidas == 0:
            corriendo = False
        
        pygame.display.flip()

        # Pantalla final o gameover

    ventana.fill((0, 0, 0))
    mensaje_final = fuente.render("¡Fin del juego!", True, (255, 255, 255))
    puntuacion_final = fuente.render(f"Puntuación final: {puntuacion}", True, (255, 255, 255))
    ventana.blit(mensaje_final, (300, 250))
    ventana.blit(puntuacion_final, (300, 300))
    pygame.display.flip()
    pygame.time.wait(3000)

    nombre = solicitar_nombre(ventana, fuente)
    guardar_clasificacion(nombre, puntuacion)
