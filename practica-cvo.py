## Tipos de datos simples/elementales
# enteros
entero = 543
print(entero)

# float - decimal
decimal = 0.43
print(decimal)

# string
cadena = "Info 2024-07-11"
cadena1 = 'Info 2024-07-11'
cadena2 = """DOCSTRING"""
cadena3 = '''DOCSTRING'''
print(cadena)

# boolean
verdadero = True
falso = False
print(verdadero)
print(falso)

# vacio, null, nulo, None, nil
vacio = None
print(vacio)

# funcion type(), que tipo de dato tiene dentro
print(type(vacio))

## Tipos de datos estructurados/complejos
# list
lista = [1,2,3,4,5,6,7,8,"algo"] # 9 elementos. Indice empieza en 0.
print(lista)
print(lista[3])
lista_lista = [[3,2,1], [7,6,5], [10,11,13]]
lista_lista.append(2)
print(lista_lista)
lista_lista[3] = 365
print(lista_lista)

# tuplas
tuplas = (1,2,3,4,5,6)
print(tuplas[2])
# tuplas[2] = 345 TypeError: 'tuple' object does not support item assignment
print(tuplas)

# set-conjunto 1,2,3
conjuntos = {1,2,3,4,5,6,7,8,9,'123','123','123'}
print(conjuntos)

# diccionarios, map, clave-valor, key-value
ciudades = {'Chaco': ['Resistencia', 'Fontana', 'Barranqueras'], 'Corrientes':'Corrientes', 'Misiones':'Posadas'}
print(ciudades['Chaco'])

# definidos por el programdor, librerias, dataframe(df)
