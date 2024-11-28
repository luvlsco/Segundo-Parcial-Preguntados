import pygame

from src.game.config import *

pygame.init()

utn_icono = pygame.image.load("assets/images/icono_utn.png")

menu = pygame.image.load("assets/images/menu_preguntados.png")
menu = pygame.transform.scale(menu, (ANCHO, ALTO))
    
imagen_pantalla_carga = pygame.image.load("assets/images/pantalla_carga.png")
imagen_pantalla_carga = pygame.transform.scale(imagen_pantalla_carga, (ANCHO, ALTO))
    
boton_jugar = pygame.image.load("assets/images/boton_jugar.png")
boton_jugar_pos = (260, 440)

boton_agregar = pygame.image.load("assets/images/boton_agregar.png")
boton_agregar_pos = (650, 525)

boton_configurar = pygame.image.load("assets/images/boton_configurar.png")
boton_configurar_pos = (10, 525)

boton_ver_top = pygame.image.load("assets/images/boton_ver_top.png")
boton_ver_top_pos = (325, 525)

pantalla_jugar = pygame.image.load("assets/images/fondo_jugar.png")
pantalla_jugar = pygame.transform.scale(pantalla_jugar, (800, 600))