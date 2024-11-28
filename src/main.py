import pygame
import sys

from src.game.config import *
from src.game.functions import *
from src.assets.sounds import *
from src.assets.images import *

from src.pantalla_carga import *
from src.menu_principal import *

pygame.init()

def inicializar_juego():
    ventana = establecer_ventana(ANCHO, ALTO) # Ruta: "src/game/functions.py"

    mostrar_pantalla_carga(ventana) # Ruta: "src/pantalla_carga.py"
    mostrar_menu_principal(ventana) # Ruta: "src/menu_principal.py"

def cerrar_juego():
    '''
    [!] Esta función hace que no sea necesario usar una variable como "corriendo/ejecutando = True" para el juego, al hacer click a la [X] de la ventana esta se cerrara de forma segura usando "sys.exit()"

    pygame.quit(): Cierra la ventana actual del juego. (Requiere una variable)
    sys.exit(): Finaliza el proceso del juego (Usado para salir del bucle principal sin necesidad de usar una variable "corriendo/ejecutando")
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()