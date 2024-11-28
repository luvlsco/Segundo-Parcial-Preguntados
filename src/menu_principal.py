# src/menu_principal.py
# Módulo que controla el menú principal del juego

import pygame

from src.assets.images import *
from src.assets.sounds import *
from src.game.functions import *
from src.ventana_jugar import *

def mostrar_menu_principal(variable_ventana: pygame.Surface) -> None:
    # Establecer el título de la ventana y reproducir la música de fondo del menú
    pygame.display.set_caption("Preguntados: Menú principal [def grupo(guido, lucas, martin)]")
    reproducir_musica("assets/sounds/music/menu_principal.mp3", 0.5, -1)

    # Rellenar el fondo con color negro
    variable_ventana.fill((0, 0, 0))

    # Mostrar el menú principal y los botones
    variable_ventana.blit(menu, (0, 0))
    variable_ventana.blit(boton_jugar, (260, 440))
    variable_ventana.blit(boton_agregar, (650, 525))
    variable_ventana.blit(boton_configurar, (10, 525))
    variable_ventana.blit(boton_ver_top, boton_ver_top_pos)

    # Actualizar la pantalla para reflejar los cambios visuales
    actualizar_pantalla()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos  # Posición del mouse al hacer clic

            # Detección de clics en los botones
            if detectar_click(boton_jugar, boton_jugar_pos, mouse_pos):
                variable_ventana = ventana_jugar()
            elif detectar_click(boton_agregar, boton_agregar_pos, mouse_pos):
                pass #variable_ventana = ventana_agregar_preguntas()
            elif detectar_click(boton_configurar, boton_configurar_pos, mouse_pos):
                pass #variable_ventana = ventana_configuracion()
            elif detectar_click(boton_ver_top, boton_ver_top_pos, mouse_pos):
                pass #variable_ventana = ventana_top()