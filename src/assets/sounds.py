# src/assets/sounds.py
# Módulo usado para manejar los sonidos que se usan dentro del juego,
# contiene las funciones generales para reproducir sonidos y las
# variables de los efectos de sonido.

import pygame

pygame.init()
pygame.mixer.init()

# Funciones generales para sonidos:
# Delay de sonido (Esperar a que termine de reproducirse el efecto de sonido)
def esperar_efecto_sonido(efecto_sonido: pygame.mixer.Sound):
    pygame.time.delay(int(efecto_sonido.get_length() * 1000))

# Efectos de sonido (assets/sounds/sfx) (.ogg, .wav)
def establecer_efecto_sonido(ruta: str, volumen: float):
    '''
    Función para reproducir efectos de sonidos dentro del juego.
    ¿Qué hace?:
        Establece efectos de sonidos en una variable a partir de los parámetros ingresados.

    ¿Qué recibe?:
        - ruta (str): Cadena que contiene la ruta del efecto de sonido (.ogg, wav)
        - volumen (float): Número flotante que controla el volumen del efecto de sonido
    '''
    efecto_sonido = pygame.mixer.Sound(ruta)
    efecto_sonido.set_volume(volumen)

    return efecto_sonido

# Música (assets/sounds/music) (.mp3)
def reproducir_musica(ruta: str, volumen: float, veces_a_reproducir: int):
    '''
    Función para reproducir música dentro del juego.

    ¿Qué hace?:
        Reproduce música a partir de los parámetros ingresados.

    ¿Qué recibe?:
        - ruta (str): Cadena que contiene la ruta de la música (.mp3)
        - volumen (float): Número flotante que indica el volúmen de la música
        - veces_a_reproducir: Número entero que indica cuantas veces se va a reproducir la música
            - -1: Reproduce la música infinitamente (bucle)
            - 0: No reproduce la música
            - 1: Reproduce la música 1 (una) vez
            - 2: Reproduce la música 2 (dos) veces
            - (int): Reproduce la música dependiendo del número entero ingresado (int)
    '''
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.set_volume(volumen)
    pygame.mixer.music.play(veces_a_reproducir)

# Variables que contienen los sonidos
efecto_sonido_apertura = establecer_efecto_sonido("assets/sounds/sfx/abrir_juego.wav", 0.6)