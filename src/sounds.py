import pygame

pygame.init()
pygame.mixer.init()

# Sonido (sfx) (WAV o OGG)
sonido_apertura = pygame.mixer.Sound("assets/sounds/sfx/abrir_juego.wav")
sonido_apertura.set_volume(0.65)
sonido_apertura_reproducido = False