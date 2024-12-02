# src/ventana_ranking.py
# Módulo que controla la ventana de ranking del botón "Ver ranking"

import pygame

from src.game.functions import *
from src.assets.images import *
from src.assets.sounds import *

def ventana_ranking(variable_ventana: pygame.Surface) -> str:
    pygame.display.set_caption("Preguntados: Ranking")

    fuente = cargar_fuente_personalizada("assets/fonts/fuente_preguntados.otf", 36)
    ruta_json = "ranking.json"
    clasificacion = cargar_clasificacion(ruta_json)
    
    boton_volver_inicio = crear_boton(
    path="assets/images/inicio.png",
    dimensiones=(50, 50),
    posicion=(20, 20),
    funcion=None
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar_juego()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver_inicio["boton_pos"].collidepoint(event.pos):
                    ui_sonido_boton.play()
                    return "ranking_volver"

        variable_ventana.blit(ventana_top, (0, 0))
        graficar_clasificacion(variable_ventana, clasificacion, fuente, (215, 155))
        variable_ventana.blit(boton_volver_inicio["surface"], boton_volver_inicio["boton_pos"].topleft)

        actualizar_pantalla()