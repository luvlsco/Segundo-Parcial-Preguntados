diccionario_contactos = {"Sara":1112345678, "Carla": 1112345678 }

def agregar_contacto( diccionario_contactos: dict, nombre: str, celular: int) -> dict :
    
    agregar = diccionario_contactos.update({nombre: celular})
     
     
     
    return agregar


agregar_contacto(diccionario_contactos, "Pedro", 1187654321 )

# print(diccionario_contactos)


def eliminnar_contacto( diccionario_contactos: dict, nombre: str):

    eliminar = diccionario_contactos.pop(nombre)


    return eliminar


# a = eliminnar_contacto(diccionario_contactos,"Pedro")
# print(diccionario_contactos)



def modificar_contacto(diccionario_contactos:dict, nombre: str, valor_modificar: int):

    diccionario_contactos[nombre] = valor_modificar




# modificar_contacto(diccionario_contactos,"Pedro", 1187654321)

# print(diccionario_contactos)


def buscar_numero_telefonico(diccionario_contactos: dict, nombre: str)-> int:

    numero_celular = diccionario_contactos.get(nombre)

    return numero_celular


# a = buscar_numero_telefonico(diccionario_contactos,"Pedro")
# print(f"El numero buscado es {a}")

def modificar_contacto(diccionario_contactos: dict, nombre: str, nuevo_nombre: str):
    
    diccionario_contactos[nuevo_nombre] = diccionario_contactos.pop(nombre)



# a = modificar_contacto(diccionario_contactos,"Sara","Guido")

# print(diccionario_contactos)


# +54 9 11 8765 4321
# +54 9 11 2345 6789
# +54 9 11 9876 5432
# +54 9 11 3456 7890
# +54 9 11 8765 1234
# +54 9 11 4567 8901
# +54 9 11 5678 9012
# +54 9 11 6789 0123
# +54 9 11 7890 1234



diccionario_puntaje_jugadores = {"Guido": 100 , "Sara":1112, "Carla": 678 }

def añadir_jugador(diccionario_puntaje_jugadores: dict, nombre: str, puntaje: int):
    
    agregar = diccionario_puntaje_jugadores.update({nombre: puntaje})





a = añadir_jugador(diccionario_puntaje_jugadores,"Pedro", 2000)






def mostrar_diccionario_ordenado( diccionario: dict):
    diccionario = list(diccionario.items())
    diccionario.sort()
    diccionario = dict(diccionario)

    return diccionario

# print(mostrar_diccionario_ordenado(diccionario_puntaje_jugadores))


# def verificar_igualdad(aaa:dict):

#     lista = []

#     lista_jugadores = list(jugadores.keys())
#     print(lista_jugadores)

#     for i in range(len(lista_jugadores)):
#         for j in range(i+1 ,len(lista_jugadores)):
#             if jugadores[lista_jugadores[i]] == jugadores[lista_jugadores[j]]:
#                 lista.append((lista_jugadores[i],lista_jugadores[j]))
    
#     return lista

# print(verificar_igualdad(jugadores))
# def verificar_igualdad(jugadores:dict):

#     lista = []

#     lista_jugadores = list(jugadores.keys())
#     print(lista_jugadores)

#     for i in range(len(lista_jugadores)):
#         for j in range(i+1 ,len(lista_jugadores)):
#             if jugadores[lista_jugadores[i]] == jugadores[lista_jugadores[j]]:
#                 lista.append((lista_jugadores[i],lista_jugadores[j]))
    
#     return lista

# print(verificar_igualdad(jugadores))
# def verificar_igualdad(jugadores:dict):

#     lista = []

#     lista_jugadores = list(jugadores.keys())
#     print(lista_jugadores)

#     for i in range(len(lista_jugadores)):
#         for j in range(i+1 ,len(lista_jugadores)):
#             if jugadores[lista_jugadores[i]] == jugadores[lista_jugadores[j]]:
#                 lista.append((lista_jugadores[i],lista_jugadores[j]))
    
#     return lista

# print(verificar_igualdad(jugadores))







# def buscar_sucursal_con_menor_generado(matriz: list) -> list:
#     """
#     Busca la sucursal que tiene lo menor generado en una matriz de notas.

#     Esta función calcula el total de los productos de cada sucursal y determina
#     cuáles tiene lo menor generado. Si hay varias sucursales con la misma cantida,
#     se incluyen todos los índices en la lista resultante.

#     Parámetros:
#         matriz (list): Matriz de notas donde cada fila representa una división
#                        y cada columna representa las notas trimestrales.

#     Retorna:
#         list: Una lista de índices de divisiones que tienen la mayor nota.
#     """
#     totales = [] 
#     for i in range(len(matriz)):
#         nota_final_por_divsion = sumar_lista(matriz[i])
#         totales.append(nota_final_por_divsion)  
    
#     menor_generado = totales[0]
#     indices = [1]  

#     for i in range(1, len(totales)-1):
#         if totales[i] < menor_generado:
#             menor_generado = totales[i]
#             indices = [i]  
#         elif totales[i] == menor_generado and i not in indices:
#             indices.append(i) 

#     return indices
