import pygame
import json
import sys

from src.game.config import *

# Funciones generales que se usan en la mayoría de módulos:
def cerrar_juego():
    '''
    Función utilizada para cerrar el juego de manera segura.

    Cuando el usuario hace clic en la [X] de la ventana, esta función maneja
    el evento de cierre de la ventana y cierra el juego de manera segura utilizando
    "pygame.quit()" y "sys.exit()".

    Se debe usar esta función al principio de los bucles principales de las ventanas
    para asegurar que el juego pueda cerrarse correctamente.
    '''
    pygame.quit()
    sys.exit()

def establecer_ventana(ancho: int, alto: int):
    return pygame.display.set_mode((ancho, alto), pygame.RESIZABLE)

def actualizar_pantalla():
    pygame.display.update()

def crear_boton(path: str, dimensiones: tuple, posicion: tuple, funcion):
    boton = {}
    boton["surface"] = pygame.image.load(path)
    boton["surface"] = pygame.transform.scale(boton["surface"], dimensiones)
    boton["boton_pos"] = pygame.Rect(posicion, dimensiones)  # Rectángulo en la posición correcta
    boton["funcion"] = funcion  # Almacenar la función sin ejecutarla
    return boton

def detectar_click(imagen, posicion, mouse_pos):
    '''
    Detecta si el mouse hizo clic dentro del área ocupada por una imagen.

    Args:
        imagen: Superficie (Surface) de Pygame que representa el botón.
        posicion: Tupla (x, y) con la posición superior izquierda de la imagen.
        mouse_pos: Tupla (x, y) con la posición del mouse.

    Returns:
        True si el clic ocurrió dentro del área de la imagen, False en caso contrario.
    '''
    x, y = posicion
    ancho, alto = imagen.get_size()
    return x <= mouse_pos[0] <= x + ancho and y <= mouse_pos[1] <= y + alto

def solicitar_nombre(ventana, fuente):
    bandera = True
    nombre = ""
    while bandera:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                bandera = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    bandera = False
                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += evento.unicode

        # Mostrar entrada de texto
        ventana.fill((0, 0, 0))
        mensaje = fuente.render("Ingrese su nombre y presione Enter:", True, (255, 255, 255))
        texto_nombre = fuente.render(nombre, True, (255, 255, 255))
        ventana.blit(mensaje, (50, 250))
        ventana.blit(texto_nombre, (50, 300))
        pygame.display.flip()

    return nombre

def guardar_clasificacion(nombre, puntuacion):
    archivo = "ranking.json"
    try:

        with open(archivo, "r") as f:
            clasificacion = json.load(f)
    except FileNotFoundError:

        clasificacion = []

    clasificacion.append({"nombre": nombre, "puntuacion": puntuacion})
    clasificacion = sorted(clasificacion, key=lambda x: x["puntuacion"], reverse=True)

    # Guardar de nuevo el archivo
    with open(archivo, "w") as f:
        json.dump(clasificacion, f, indent=4)