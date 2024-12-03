import pygame

from src.game.functions import *
from src.assets.images import *
from src.assets.sounds import *

def agregar_preguntas(variable_ventana, diccionario_preguntas):
        '''
    Función para agregar preguntas al juego.

    ¿Qué hace?:
        - Permite el ingreso de nuevas preguntas y sus respectivas opciones.
        - Pide la opcion correcta y valida que la respuesta sea valida.
        - Agrega la pregunta y opciones al diccionario de preguntas.
        - Divide todo en pasos.

    ¿Qué recibe?:
        - variable_ventana: Donde se grafica la ventana.
        - diccionario_preguntas: Lista con las preguntas

    ¿Qué retorna?:
        - Nada, pero modifica la lista con las preguntas.
    '''
        entrada = ""
        mensaje = "Ingrese la pregunta:"
        paso = 1
        respuestas_nuevas = []
        respuesta_correcta = None
        pregunta_nueva = None

        while True:
            configurar_fps(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cerrar_juego()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  
                        if paso == 1:
                            pregunta_nueva = entrada
                            mensaje = "Ingrese la respuesta A:"
                            entrada = ""
                            paso += 1
                        elif 2 <= paso <= 5: 
                            respuestas_nuevas.append(entrada)
                            entrada = ""
                            if paso == 5:
                                mensaje = "Ingrese la opción correcta (0, 1, 2, 3):"
                                paso += 1
                            else:
                                mensaje = f"Ingrese la respuesta {chr(65 + paso - 1)}:"
                                paso += 1
                        elif paso == 6: 
                            if entrada.isdigit() and int(entrada) in [0, 1, 2, 3]:
                                respuesta_correcta = int(entrada)  # Asigna como entero
                                nueva_pregunta = {
                                    "pregunta": pregunta_nueva,
                                    "opciones": respuestas_nuevas,
                                    "respuesta_correcta": respuesta_correcta
                                }
                                diccionario_preguntas.append(nueva_pregunta)
                                print("Pregunta agregada:", nueva_pregunta)  
                                return  
                            else:
                                mensaje = "Opción incorrecta. Ingrese 0, 1, 2, 3"
                            entrada = ""
                    elif event.key == pygame.K_BACKSPACE:
                        entrada = entrada[:-1]
                    else:
                        entrada += event.unicode

            variable_ventana.blit(ventana_agregar_pregunta, (0, 0))
            fuente = cargar_fuente_personalizada("assets/fonts/fuente_preguntados.otf", 26)
            texto_mensaje = fuente.render(mensaje, True, (0, 0, 0))  
            variable_ventana.blit(texto_mensaje, (50, 45))

            texto_entrada = fuente.render(entrada, True, (0, 0, 255))  
            variable_ventana.blit(texto_entrada, (50, 95))
            actualizar_pantalla()