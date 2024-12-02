# src/game/config.py
# Módulo encargado de gestionar las configuraciones generales del juego,
# como la inicialización de Pygame y las configuraciones predeterminadas del juego.

# Este módulo se importa en todos los demás módulos del juego para evitar la repetición
# de la inicialización.

import pygame

# Inicialización de Pygame
pygame.init() # Inicializa todos los módulos de Pygame
pygame.mixer.init() # Inicializa el módulo de audio de Pygame

# Configuraciones del juego
ANCHO = 800
ALTO = 600
FPS = 30

# Configuraciones de la partida (Pueden modificarse)
vidas = 3
puntuacion_correcta = 1