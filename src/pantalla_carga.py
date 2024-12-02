# src/pantalla_carga.py
# Módulo que controla la pantalla de carga que se muestra antes del menú principal

from src.game.config import *
from src.game.functions import *
from src.assets.images import *
from src.assets.sounds import *

def mostrar_pantalla_carga(variable_ventana: pygame.Surface) -> None:
    '''
    Función que muestra la pantalla de carga antes del menú principal.

    ¿Qué hace?:
        Muestra la imagen de la pantalla de carga y establece el icono de la ventana que se usa en el juego, reproduce el sonido de apertura y pasa al menú principal.
    
    ¿Qué recibe?:
        - variable_ventana (pygame.Surface): La ventana donde se renderiza la pantalla de carga.
    '''
    # Establecer título e icono de la ventana, reproducir sonido de apertura, mostrar imagen de carga y actualizar la pantalla
    pygame.display.set_caption("Preguntados: Cargando...")
    pygame.display.set_icon(utn_icono)
    variable_ventana.blit(imagen_pantalla_carga, (0, 0))
    efecto_sonido_apertura.play()
    actualizar_pantalla()

    # Esperar a que termine de reproducirse el sonido de apertura
    esperar_efecto_sonido(efecto_sonido_apertura)