# src/main.py
# Módulo principal que carga la ventana del juego, la variable de la ventana se usa en todas las funciones de tipo "ventana_" bajo el nombre "variable_ventana"

from src.game.config import *
from src.game.functions import *
from src.assets.sounds import *
from src.assets.images import *

from src.pantalla_carga import *
from src.menu_principal import *

def inicializar_juego():
    # Se carga/establece la ventana en una variable. Esto luego pasa a las funciones de diferentes ventanas del juego como "variable_ventana" (Solo se establece una vez para evitar repetir código).
    ventana = establecer_ventana(ANCHO, ALTO) # Ruta: "src/game/functions.py"

    # Se muestra primero la pantalla de carga, después se muestra el menú principal. Como mencioné antes, se usa la variable de la ventana en el parámetro de la función para navegar por las diferentes ventanas del juego.
    mostrar_pantalla_carga(ventana) # Ruta: "src/pantalla_carga.py"
    mostrar_menu_principal(ventana) # Ruta: "src/menu_principal.py"