import pygame
import random

from src.game.config import *
from src.game.questions import *
from src.game.functions import *

from src.assets.images import *
from src.assets.sounds import *

#puntuacion = 0
puntuacion_correcta = 1
#vidas = 3

def ventana_jugar(variable_ventana: pygame.Surface) -> str:
    # Cambiar el título de la ventana, establecer la fuente y reproducir la música
    pygame.display.set_caption("Preguntados: Jugando")
    fuente = pygame.font.Font(None, 36)
    reproducir_musica("assets/sounds/music/ventana_jugar.mp3", 1, -1)

    global puntuacion_correcta, vidas, puntuacion
    puntuacion = 0
    vidas = 3
    pregunta_actual = 0
    mostrando_respuesta = False
    color_respuesta = (255, 255, 0)
    random.shuffle(diccionario_preguntas)

    corriendo_juego = True
    while corriendo_juego:
        cerrar_juego()

        variable_ventana.blit(pantalla_jugar, (0, 0))

        # Procesar eventos de clic
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN and not mostrando_respuesta:
                mouse_pos = pygame.mouse.get_pos()
                for i, opcion_rect in enumerate(opciones_rects):
                    if opcion_rect.collidepoint(mouse_pos):

                        if i == diccionario_preguntas[pregunta_actual]["respuesta_correcta"]:
                            puntuacion += puntuacion_correcta
                            color_respuesta = ((0, 255, 0))
                            efecto_sonido_correcto.play()
                        else:
                            vidas -= 1
                            color_respuesta = ((255, 0, 0))
                            efecto_sonido_incorrecto.play()
                        mostrando_respuesta = True
                        break

        # Mostrar pregunta
        pregunta_texto = fuente.render(diccionario_preguntas[pregunta_actual]["pregunta"], True, ((0, 0, 0)))
        variable_ventana.blit(pregunta_texto, (50, 50))

        # Mostrar opciones
        opciones_rects = []
        for i, opcion in enumerate(diccionario_preguntas[pregunta_actual]["opciones"]):
            opcion_texto = fuente.render(opcion, True, (0, 0, 0))
            opcion_rect = opcion_texto.get_rect(topleft=(50, 150 + i * 50))
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
                corriendo_juego = False

        # Mostrar puntuación y vidas
        puntuacion_texto = fuente.render(f"Puntuación: {puntuacion}", True, (255, 255, 255))
        vidas_texto = fuente.render(f"Vidas: {vidas}", True, (235,66, 112))
        variable_ventana.blit(puntuacion_texto, (50, 500))
        variable_ventana.blit(vidas_texto, (650, 500))

        # Revisar si se acabaron las vidas
        if vidas == 0:
            corriendo_juego = False

        actualizar_pantalla()

    # Pantalla final (Game Over)
    variable_ventana.fill((0, 0, 0))
    mensaje_final = fuente.render("¡Fin del juego!", True, (255, 255, 255))
    puntuacion_final = fuente.render(f"Puntuación final: {puntuacion}", True, (255, 255, 255))
    variable_ventana.blit(mensaje_final, (300, 250))
    variable_ventana.blit(puntuacion_final, (300, 300))
    actualizar_pantalla()
    pygame.time.wait(3000)

    nombre = solicitar_nombre(variable_ventana, fuente)
    guardar_clasificacion(nombre, puntuacion)

    # Cuando toda la ventana termina de ejecutarse retorna esta cadena a la variable usada en el menú principal "src/menu_principal.py".
    # Esto es útil para evitar el uso de clases o una lista de pantallas, ya que se maneja
    # de manera más simple todas las ventanas del juego.
    return "ventana_jugar_completada"