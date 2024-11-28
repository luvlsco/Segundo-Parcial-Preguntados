# src/pantalla_carga.py
# Módulo que controla la pantalla de carga que se muestra antes del menú principal

from src.game.functions import *
from src.assets.images import *
from src.assets.sounds import *

def mostrar_pantalla_carga(variable_ventana: pygame.Surface) -> None:
    '''
    Función que muestra la pantalla de carga antes del menú principal.

    ¿Qué hace?:
    1. Establece el título y el icono de la ventana del juego.
    2. Reproduce el efecto de sonido de apertura.
    3. Muestra la imagen de carga en la ventana.
    4. Actualiza la pantalla para mostrar la imagen de carga.
    5. Espera a que termine de reproducirse el sonido de apertura antes de mostrar el menú principal.
    
    ¿Qué recibe?:
        - variable_ventana (pygame.Surface): La ventana donde se renderiza la pantalla de carga.
    '''
    # Establecer título e icono de la ventana, reproducir sonido de apertura, mostrar imagen de carga y actualizar la pantalla
    pygame.display.set_caption("Preguntados: Cargando...")
    pygame.display.set_icon(utn_icono)
    efecto_sonido_apertura.play()
    variable_ventana.blit(imagen_pantalla_carga, (0, 0))
    actualizar_pantalla()

    # Esperar a que termine de reproducirse el sonido de apertura
    esperar_efecto_sonido(efecto_sonido_apertura)