import pygame

from src.game.functions import *
from src.game.questions import *
from src.assets.images import *
from src.assets.sounds import *

from src.ventana_agregar import *

def ventana_agregar_preguntas(variable_ventana: pygame.Surface) -> str:
    pygame.display.set_caption("Preguntados: Agregar pregunta")

    boton_volver_inicio = crear_boton(
        path="assets/images/inicio.png",
        dimensiones=(50,50),
        posicion=(20, 20),
        funcion=None
        )

    boton_agregar_pregunta = crear_boton(
        path="assets/images/boton_agregar.png",
        dimensiones=(200, 100),
        posicion=(300, 300),
        funcion=lambda:agregar_preguntas(variable_ventana, diccionario_preguntas)
        )

    while True:
        configurar_fps(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar_juego()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_agregar_pregunta["boton_pos"].collidepoint(event.pos):
                    ui_sonido_boton.play()
                    boton_agregar_pregunta["funcion"]()

                elif boton_volver_inicio["boton_pos"].collidepoint(event.pos):
                    ui_sonido_boton.play()
                    return "agregar_preguntas_volver"
                    
        # Dibujar fondo y botón
        variable_ventana.blit(ventana_pregunta, (0, 0))
        variable_ventana.blit(boton_agregar_pregunta["surface"], boton_agregar_pregunta["boton_pos"].topleft)
        variable_ventana.blit(boton_volver_inicio["surface"], boton_volver_inicio["boton_pos"].topleft)
        actualizar_pantalla()