import pygame

from src.game.config import *
from src.game.questions import *
from src.game.functions import *

from src.assets.images import *
from src.assets.sounds import *

def ventana_configuracion(variable_ventana: pygame.Surface) -> str:
    pygame.display.set_caption("Preguntados: Configuración")
    variable_ventana.blit(imagen_ventana_configuracion, (0, 0))

    boton_volver_inicio = crear_boton(
        path="assets/images/inicio.png",
        dimensiones=(50,50),
        posicion=(20, 20),
        funcion=lambda: print("test"))

    boton_configuracion = crear_boton(
        path="assets/images/boton_configurar.png", # Ruta de la imagen del botón
        dimensiones=(200, 100),                    # Tamaño del botón (ancho, alto)
        posicion=(300, 300),                       # Posición del botón (x, y)
        funcion=lambda:print("test_2")          # Función para agregar preguntas
    )

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_juego()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                if boton_configuracion["boton_pos"].collidepoint(evento.pos):
                    boton_configuracion["funcion"]()
                
                elif boton_volver_inicio["boton_pos"].collidepoint(evento.pos):
                    boton_volver_inicio["funcion"]()
                    
        # Dibujar fondo y botón
        variable_ventana.blit(imagen_ventana_configuracion, (0, 0))
        variable_ventana.blit(boton_configuracion["surface"], boton_configuracion["boton_pos"].topleft)
        variable_ventana.blit(boton_volver_inicio["surface"], boton_volver_inicio["boton_pos"].topleft)      

        actualizar_pantalla()