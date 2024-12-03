#src/game/functions.py

# Módulo usado para almacenar las funciones generales y específicas del juego

import pygame
import json
import sys

from src.game.config import *

# Funciones generales que se usan en la mayoría de módulos:
def cerrar_juego() -> None:
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

def configurar_fps(FPS: int) -> None:
    '''
    Función utilizada para configurar los FPS (Frames por segundo) del juego
    
    ¿Qué hace?:
        Limita los FPS del juego, puede usarse en diferentes ventanas (para ahorrar recursos de la computadora del usuario)

    ¿Qué recibe?:
        - FPS: Número entero que define los FPS para limitarlos.
    '''
    clock = pygame.time.Clock()
    clock.tick(FPS)

def establecer_ventana(ancho: int, alto: int) -> pygame.Surface:
    '''
    Función para establecer una ventana de pygame

    ¿Qué hace?:
        Establece/configura una ventana de pygame.
    ¿Qué recibe?:
        - ancho (int): Número entero que define el ancho de la ventana
        - alto (int): Número entero que define el alto de la ventana
    ¿Qué retorna?:
        pygame.Surface: La superficie de la ventana establecida.
    '''
    return pygame.display.set_mode((ancho, alto), pygame.RESIZABLE)

def actualizar_pantalla() -> None:
    '''
    Función simple que actualiza la ventana de Pygame.

    ¿Por qué es necesaria?:
        Con fines estéticos para el código, existen dos formas de actualizar las ventanas de Pygame:
            - pygame.display.update()
            - pygame.display.flip()
        Para no usar ambos en el código, se creó esta función para usar uno y mejorar la visibilidad cuando se actualiza la pantalla.
    '''
    pygame.display.update()

def cargar_fuente_personalizada(ruta: str, tamaño: int) -> pygame.font.Font | None:
    '''
    Función para cargar una fuente de texto.

    ¿Qué hace?:
        Carga una fuente para usarla en el juego.

    ¿Qué recibe?:
        - ruta (str): Cadena que contiene la ruta de la fuente
        - tamaño (int): Número entero que configura el tamaño de la fuente

    ¿Qué retorna?:
        - pygame.font.Font: La fuente cargada
        - None: Nada si la fuente no existe o no se encuentra en la ruta
    '''
    try:
        return pygame.font.Font(ruta, tamaño)
    except FileNotFoundError:
        return None

def crear_boton(path: str, dimensiones: tuple, posicion: tuple, funcion):
    
        '''
    Función para crear un botón.

    ¿Qué hace?:
        Crea un boton.

    ¿Qué recibe?:
        - path (str): Directorio que contiene la imagen a utilizar.
        - dimensiones (tuple): El tamaño del botón (Ancho x largo).

    ¿Qué retorna?:
        - botón con las especificaciones otorgadas.
    '''
        
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

def pedir_entero(mensaje: str, mensaje_error: str, minimo: int | bool = False, maximo: int | bool = False) -> int:
    """
    Pide un mensaje, un mensaje de error y límites opcionales mínimo y máximo.
    Muestra el mensaje y solicita que se ingrese un entero. Si el valor ingresado no está
    dentro de los límites especificados, se vuelve a pedir con el mensaje de error.

    Devuelve:
        Un número entero que cumple con los límites especificados.
    """

    while True:
        try:
            retorno = int(input(mensaje))
            if (minimo != False and retorno < minimo) or (maximo != False and retorno > maximo):
                print(mensaje_error)
            else:
                return retorno
            
        except ValueError:
            print(mensaje_error)



# Funciones específicas que se usan en algunos módulos

def solicitar_nombre(ventana, fuente):
        '''
    Función que solicita un nombre.

    ¿Qué hace?:
        - Solicita una cadena de caracteres / nombre.
        - Baraja distintas posibilidades de eventos. Pudiendo cerrar el juego, escribir el nombre y poder borrar un caracter en caso de equivocación.
        - Muestra en pantalla las consignas

    ¿Qué recibe?:
        - ventana: variable definida anteriormente que hace referencia a la ventana del juego en si.
        - fuente: fuente de texto utilizada para mostrar el mensaje en pantalla. 

    ¿Qué retorna?:
        - nombre: guarda la variable nombre con los datos ingresados por el usuario.
    '''
        
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
        '''
    Función para guardar la clasificación.

    ¿Qué hace?:
        - Guarda la clasificacion después de cada partida, agregando el nombre del jugador y el puntaje obtenido.

    ¿Qué recibe?:
        - nombre: variable obtenida en la funcion de solicitar_nombre.
        - puntuación: puntuación final obtenida en el juego.

    ¿Qué retorna?:
        - None, simplemente agrega el nombre y la puntuacion de cada jugador en el archivo ranking.json
    '''
        archivo = "ranking.json"
        try:
            with open(archivo, "r") as f: # Con r abre el archivo en modo de lectura.
                clasificacion = json.load(f)
        except FileNotFoundError:
            clasificacion = [] # Si el archivo no existe, lo crea.

        clasificacion.append({"nombre": nombre, "puntuacion": puntuacion})
        clasificacion = sorted(clasificacion, key=lambda x: x["puntuacion"], reverse=True)

        # Guardar de nuevo el archivo
        with open(archivo, "w") as f: # Con w abre el archivo en modo de escritura.
            json.dump(clasificacion, f, indent=4) # indent = 4 mejora la lectura haciendolo mas comodo de leer, es simplemente por comodidad.

def cargar_clasificacion(ruta_json):
        '''
    Función que carga la clasificación / ranking.

    ¿Qué hace?:
        Carga la tabla de clasificación y abre el archivo en modo de lectura.

    ¿Qué recibe?:
        - ruta_json: ruta que contiene el archivo .json

    ¿Qué retorna?:
        - devuelve el contenido del archivo .json en forma de lista.
        - si hay un error, devuelve una lista vacia
    '''
        try:
            with open(ruta_json, 'r') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {ruta_json}")
            return []
        except json.JSONDecodeError:
            print(f"Error: El archivo {ruta_json} no tiene un formato JSON válido")
            return []

def graficar_clasificacion(ventana, clasificacion, fuente, posicion_inicial):
        '''
    Función que grafica la tabla de clasificacion.

    ¿Qué hace?:
        - Toma del archivo con la lista de jugadores los nombres y la puntuacion.
        - Muestra a los 10 primeros jugadores enumerados según su puntaje.
        - Posiciona a los jugadores en nuevas lineas utilizando un desplazamiento vertical (y_offset) empezando desde "posicion inicial".

    ¿Qué recibe?:
        - Ventana: ventana del juego donde se dibujará la tabla de clasificación.
        - Clasificacion: La lista con los datos de los jugadores.
        - Fuente: fuente a utilizar para renderizar el texto.
        - Posicion_inicial: una tupla que utiliza (x, y) para indicar donde se empieza a dibujar el ranking.

    ¿Qué retorna?:
        - Nada, solo grafica la tabla de posiciones.
    '''
        y_offset = 0
        for indice, jugador in enumerate(clasificacion[:10]):
            texto = f"{indice + 1}. {jugador['nombre']} - {jugador['puntuacion']} puntos"
            texto_render = fuente.render(texto, True, (255, 255, 255))
            ventana.blit(texto_render, (posicion_inicial[0], posicion_inicial[1] + y_offset))
            y_offset += 40