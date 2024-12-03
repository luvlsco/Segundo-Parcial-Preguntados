# src/menu_principal.py
# Módulo que controla el menú principal del juego

import pygame
from src.game.config import *
from src.game.functions import *
from src.assets.images import *
from src.assets.sounds import *

from src.ventana_jugar import *
from src.ventana_configuracion import *
from src.ventana_ranking import *
from src.ventana_agregar_preguntas import *

def mostrar_menu_principal(variable_ventana: pygame.Surface) -> pygame.Surface:
    '''
    Función que carga el menú principal con todas las opciones disponibles.

    ¿Qué hace?:
        - Muestra el menú con los distintos botones interactivos.
        - Permite al usuario navegar entre las distintas ventanas, pudiendo configurar el juego, agregar preguntas o ver el ranking con los 10 mejores puntajes.

    ¿Qué recibe?
        - variable_ventana: Donde se grafica la ventana con los elementos visuales.
        
    '''
    # Establecer el título de la ventana y reproducir la música de fondo del menú
    pygame.display.set_caption("Preguntados: Menú principal [def grupo(guido, lucas, martin)]")
    reproducir_musica("assets/sounds/music/menu_principal.mp3", 1, -1, False)

    # Mostrar el menú principal y los botones
    variable_ventana.fill((0, 0, 0))
    variable_ventana.blit(menu, (0, 0))
    variable_ventana.blit(boton_jugar, (260, 440))
    variable_ventana.blit(boton_agregar, (650, 525))
    variable_ventana.blit(boton_configurar, (10, 525))
    variable_ventana.blit(boton_ver_top, boton_ver_top_pos)
    actualizar_pantalla()

    while True:
        configurar_fps(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar_juego()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos # Posición del mouse al hacer clic

            # Funciones de cada botón del menú
                # [Jugar]
                if detectar_click(boton_jugar, boton_jugar_pos, mouse_pos):
                    ui_sonido_boton_jugar.play()
                    estado_ventana_jugar = ventana_jugar(variable_ventana)

                    if estado_ventana_jugar == "ventana_completada":
                        mostrar_menu_principal(variable_ventana)

                # [Agregar preguntas]
                elif detectar_click(boton_agregar, boton_agregar_pos, mouse_pos):
                    ui_sonido_boton.play()
                    estado_ventana_agregar_preguntas = ventana_agregar_preguntas(variable_ventana)

                    if estado_ventana_agregar_preguntas == "agregar_preguntas_volver":
                        mostrar_menu_principal(variable_ventana)

                # [Configuración]
                elif detectar_click(boton_configurar, boton_configurar_pos, mouse_pos):
                    ui_sonido_boton.play()
                    estado_ventana_configuracion = ventana_configuracion(variable_ventana)

                    if estado_ventana_configuracion == "configuracion_volver":
                        mostrar_menu_principal(variable_ventana)

                # [Ranking / Top]
                elif detectar_click(boton_ver_top, boton_ver_top_pos, mouse_pos):
                    ui_sonido_boton_ranking.play()
                    estado_ventana_ranking = ventana_ranking(variable_ventana)
                    
                    if estado_ventana_ranking == "ranking_volver":
                        mostrar_menu_principal(variable_ventana)