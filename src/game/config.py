# src/game/config.py
# Se inicializan los módulos de Pygame en este módulo "config" para evitar
# repetir su inicialización en otros archivos.
# Este módulo se importa en todos los archivos del juego.
import pygame

pygame.init() # Inicializa todos los módulos de Pygame
pygame.mixer.init() # Inicializa el módulo de audio de Pygame

# Configuraciones del juego
ANCHO = 800
ALTO = 600