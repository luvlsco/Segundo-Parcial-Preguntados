# src/assets/images.py
# Módulo usado para manejar las imagenes que se usan dentro del juego,
# contiene las funciones generales para cargar imagenes y las
# variables que almacenan esas imagenes.

import pygame

from src.game.config import *

# Función general para imágenes:
# Cargar imagenes (Ruta: assets/images)
def cargar_imagen(ruta: str, ancho: int | None, alto: int | None) -> pygame.Surface:
    '''
    Función para cargar una imagen en Pygame y, opcionalmente, redimensionarla.

    ¿Qué hace?:
        Carga una imagen desde la ruta proporcionada y la redimensiona
        si se especifican nuevos valores de ancho y alto.

    ¿Qué recibe?:
        - ruta (str): Cadena que contiene la ruta del archivo de imagen.
        - ancho (int | None): Ancho de la imagen. Si se proporciona el entero, la imagen se redimensiona.
        - alto (int | None): Alto de la imagen. Si se proporciona el entero, la imagen se redimensiona.

    ¿Qué retorna?:
        - imagen_cargada: La imagen cargada (y redimensionada si es necesario).
    '''
    imagen_cargada = pygame.image.load(ruta)
    if ancho != None and alto != None:
        imagen_cargada = pygame.transform.scale(imagen_cargada, (ANCHO, ALTO))

    return imagen_cargada

# <!> Imágenes:
# Pantalla de carga y extras
utn_icono = cargar_imagen("assets/images/icono_utn.png", None, None)
imagen_pantalla_carga = cargar_imagen("assets/images/pantalla_carga.png", ANCHO, ALTO)

# Menú pricipal y botones del menú principal
menu = cargar_imagen("assets/images/menu_preguntados.png", ANCHO, ALTO)
boton_jugar = cargar_imagen("assets/images/boton_jugar.png", None, None)
boton_agregar = cargar_imagen("assets/images/boton_agregar.png", None, None)
boton_configurar = cargar_imagen("assets/images/boton_configurar.png", None, None)
boton_ver_top = cargar_imagen("assets/images/boton_ver_top.png", None, None)

# Ventana del juego ("Menú principal" -> "Jugar")
pantalla_jugar = cargar_imagen("assets/images/fondo_jugar.png", ANCHO, ALTO)

# Ventana de la configuración del juego ("Menú principal" -> "Cambiar opciones")
imagen_ventana_configuracion = cargar_imagen("assets/images/fondo_configurar.jpg", ANCHO, ALTO)

# Ventana del ranking del juego ("Menú principal" -> "Ver ranking")
ventana_top = cargar_imagen("assets/images/fondo_ranking.jpg", ANCHO, ALTO)

# Ventana de agregar preguntas ("Menú principal" -> "Agregar preguntas")
ventana_pregunta = cargar_imagen("assets/images/fondo_configurar.jpg", ANCHO, ALTO)
ventana_agregar_pregunta = cargar_imagen("assets/images/fondo_agregar_pregunta.png", ANCHO, ALTO)

# <!> Variables de posicionamiento:
# Botones del menú principal
boton_jugar_pos = (260, 440)
boton_agregar_pos = (650, 525)
boton_configurar_pos = (10, 525)
boton_ver_top_pos = (325, 525)