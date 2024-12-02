# src/assets/sounds.py
# Módulo usado para manejar los sonidos que se usan dentro del juego,
# contiene las funciones generales para reproducir sonidos y las
# variables que almacenan los efectos de sonido.

import pygame

from src.game.config import *

# Funciones generales para sonidos:
# Delay de sonido (Esperar a que termine de reproducirse el efecto de sonido)
def esperar_efecto_sonido(efecto_sonido: pygame.mixer.Sound) -> None:
    pygame.time.delay(int(efecto_sonido.get_length() * 1000))

# Efectos de sonido (Ruta: assets/sounds/sfx)
def cargar_efecto_sonido(ruta: str, volumen: float) -> pygame.mixer.Sound:
    '''
    Función para reproducir efectos de sonidos dentro del juego.
    ¿Qué hace?:
        Establece efectos de sonidos en una variable a partir de los parámetros ingresados.

    ¿Qué recibe?:
        - ruta (str): Cadena que contiene la ruta del efecto de sonido (.ogg, wav)
        - volumen (float): Número flotante que controla el volumen del efecto de sonido
    
    ¿Qué retorna?:
        - efecto_sonido: El efecto de sonido cargado.
    '''
    efecto_sonido = pygame.mixer.Sound(ruta)
    efecto_sonido.set_volume(volumen)

    return efecto_sonido

# Música (assets/sounds/music)
def reproducir_musica(ruta: str, volumen: float, veces_a_reproducir: int, forzar: bool) -> None:
    '''
    Función para reproducir música dentro del juego.

    ¿Qué hace?:
        Reproduce música a partir de los parámetros ingresados.

    ¿Qué recibe?:
        - ruta (str): Cadena que contiene la ruta de la música (.mp3)
        - volumen (float): Número flotante que indica el volumen de la música
        - veces_a_reproducir: Número entero que indica cuantas veces se va a reproducir la música
            - -1: Reproduce la música infinitamente (bucle)
            - 0: No reproduce la música
            - 1: Reproduce la música 1 (una) vez
            - 2: Reproduce la música 2 (dos) veces
            - (int): Reproduce la música dependiendo del número entero ingresado (int)
        - forzar (bool): Forzar el cambio de música o no, esto es útil para que la música no se reinicie al cambiar de ventanas.
    
    ¿Qué retorna?:
        No retorna nada, las músicas de pygame se cargan y reproducen en el momento, ni siquiera es necesario almacenarlas en una variable.
    '''
    if forzar or not pygame.mixer.music.get_busy():
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.set_volume(volumen)
        pygame.mixer.music.play(veces_a_reproducir)

# Variables que contienen los sonidos
efecto_sonido_apertura = cargar_efecto_sonido("assets/sounds/sfx/abrir_juego.wav", 0.75)
efecto_sonido_correcto = cargar_efecto_sonido("assets/sounds/sfx/correcto.mp3", 1)
efecto_sonido_incorrecto = cargar_efecto_sonido("assets/sounds/sfx/incorrecto.mp3", 1)

# UI (User Interface)
ui_sonido_boton = cargar_efecto_sonido("assets/sounds/sfx/ui_sonido_boton.mp3", 1)
ui_sonido_boton_jugar = cargar_efecto_sonido("assets/sounds/sfx/ui_sonido_boton_jugar.mp3", 1)
ui_sonido_boton_ranking = cargar_efecto_sonido("assets/sounds/sfx/ui_sonido_boton_ranking.wav", 1)