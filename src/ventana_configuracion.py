# src/ventana_configuracion.py
# Módulo que controla la ventana principal del botón "Cambiar opciones"

import pygame

from src.game.functions import *
from src.assets.images import *
from src.assets.sounds import *

from src.ventana_configurar_juego import *

def ventana_configuracion(variable_ventana: pygame.Surface) -> str:
    '''
    Función que muestra la ventana para configurar el juego.

    ¿Qué hace?:
        - Crea los botones para volver al inicio y para poder configurar el juego.
        - Detecta los eventos, si el usuario cierra el juego o si clickea los botones.
        - Dibuja los elementos con blit 

    ¿Qué recibe?:
        - variable_ventana: Donde se grafica la ventana.

    ¿Qué retorna?:
        - configuracion_volver: si el usuario presiona el boton de volver al inicio, lo hace y guarda los valores introducidos.
    '''
    pygame.display.set_caption("Preguntados: Configuración")
    variable_ventana.blit(imagen_ventana_configuracion, (0, 0))

    boton_volver_inicio = crear_boton(
        path="assets/images/inicio.png",
        dimensiones=(50,50),
        posicion=(20, 20),
        funcion=None
        )

    boton_configuracion = crear_boton(
        path="assets/images/boton_configurar.png",
        dimensiones=(200, 100),
        posicion=(300, 300),
        funcion=lambda:ventana_configurar_juego(variable_ventana)
        )

    while True:
        configurar_fps(FPS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_juego()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_configuracion["boton_pos"].collidepoint(evento.pos):
                    ui_sonido_boton.play()
                    boton_configuracion["funcion"]()

                elif boton_volver_inicio["boton_pos"].collidepoint(evento.pos):
                    ui_sonido_boton.play()
                    return "configuracion_volver"

        # Dibujar fondo y botón
        variable_ventana.blit(imagen_ventana_configuracion, (0, 0))
        variable_ventana.blit(boton_configuracion["surface"], boton_configuracion["boton_pos"].topleft)
        variable_ventana.blit(boton_volver_inicio["surface"], boton_volver_inicio["boton_pos"].topleft)      

        actualizar_pantalla()