# src/ventana_configurar_juego.py
# Módulo que controla la ventana secundaria del botón "Cambiar opciones"

import src.game.config as config

from src.game.functions import *
from src.assets.images import *
from src.assets.sounds import *

def ventana_configurar_juego(variable_ventana: pygame.Surface) -> str:
    '''
    Función que muestra la ventana que pide los valores para configurar.

    ¿Qué hace?:
        - Solicita dos valores, uno para los puntos por respuesta correcto y otro para la cantidad de vidas.
        - Actualiza los valores de vida y puntuacion por respuesta correcta.
        - Muestra las consignas en pantalla.
        - Gestiona eventos ejecutables.

    ¿Qué recibe?:
        - variable_ventana: Donde se renderiza la ventana.
    
    ¿Qué retorna?:
        - configurar_juego_volver: Indica que se terminó de configurar y vuelve al inicio.
    '''
    
    global puntuacion_correcta, vidas
    fuente = cargar_fuente_personalizada("assets/fonts/fuente_preguntados.otf", 40)
    entrada = ""
    mensaje = "Ingrese puntos por respuesta:"
    posicion = (150, 200)
    paso = 1
    
    variable_ventana.blit(imagen_ventana_configuracion, (0, 0))

    while True:
        configurar_fps(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cerrar_juego()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if paso == 1:  
                        config.puntuacion_correcta = int(entrada) if entrada.isdigit() else 1
                        print(f"Nuevo valor de puntuacion_correcta: {config.puntuacion_correcta}")
                        entrada = "" 
                        mensaje = "Ingrese vidas iniciales:"
                        paso = 2
                    elif paso == 2:  
                        config.vidas = int(entrada) if entrada.isdigit() else 3
                        print(f"Nuevo valor de vidas: {config.vidas}")
                        return "configurar_juego_volver"

                elif event.key == pygame.K_BACKSPACE:
                    entrada = entrada[:-1]

                elif event.unicode.isdigit():
                    entrada += event.unicode

        variable_ventana.blit(imagen_ventana_configuracion, (0, 0))
        texto = fuente.render(mensaje, True, (255, 255, 255))
        entrada_texto = fuente.render(entrada, True, (0, 255, 0))
        variable_ventana.blit(texto, posicion)
        variable_ventana.blit(entrada_texto, (posicion[0], posicion[1] + 50))

        actualizar_pantalla()