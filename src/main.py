import pygame
import sys

from src.config import *


pygame.init()

def inicializar_juego():
    '''
    Función para iniciar el juego en una ventana.

    ¿Qué hace?:
        Establece una resolución de 800x600 (ANCHO x ALTO) para el juego y un titulo personalizado, el usuario puede redimensionar su tamaño usando el mouse.
    '''
    pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)
    pygame.display.set_caption("Preguntados [def grupo(guido, lucas, martin)]")

def cerrar_juego():
    '''
    Función que maneja el cierre de la ventana del juego.

    Esta función revisa los eventos de Pygame, si detecta que el usuario
    cierra la ventana del juego (Por ejemplo: al hacer clic en la "X"),
    se termina el juego de forma segura.

    pygame.quit(): Cierra la ventana actual del juego.
    sys.exit(): Finaliza el proceso del juego (Usado para salir del bucle principal)
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()