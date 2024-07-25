# from functools import reduce

# inmutable
# tupla = (1, 2, 3, 4, 5)

# suma = sum(tupla)
# longitud = len(tupla)
# maximo = max(tupla)
# minimo = min(tupla)
# ordenar = tuple(sorted(tupla))
# reversa = tuple(reversed(tupla)) # tupla[::-1]
# enumerar = tuple(enumerate(tupla))
# mapear = tuple(map(lambda x: x + 3, tupla))
# mapRed = reduce(lambda x, y: x + y, tupla)
# filtrado = tuple(filter(lambda x: x % 2 == 0, tupla))


# print("Suma: ", suma)
# print("Longitud: ", longitud)
# print("Maximo: ", maximo)
# print("Minimo: ", minimo)
# print("Ordenado: ", ordenar)
# print("Reversa: ", reversa)
# print("Enumerar: ", enumerar)
# print("mapear: ", mapear)
# print("mapRed: ", mapRed)
# print("Filtrado: ", filtrado)


# any() all()
# tupla = (False, False, True, False) # 0|False|None, 1...|True|

# any_list = any(tupla) # Verifica que aunque sea 1 elemento esta en True
# print("Any:", any_list)

# all_list = all(tupla) # Verifica que TODOS los elementos esten en True
# print("All:", all_list) # A >= B ##### <= != > < or xor and not

# zip()
# tupla_1 = (1,2,3)
# tupla_2 = ('a','b','c')

# tupla_cpx = tuple(zip(tupla_1, tupla_2))
# print(tupla_cpx)

# insert() remove() append() pop() count()
tupla = (1,2,3,4,5,4,4,4,4)
lista = list(tupla) # Defini una nueva variable del tipo lista
lista.insert(0, 38) # Le aplique el cambio que necesita
tupla = tuple(lista) # Recrear una nueva variable del tipo lista con la modificacion
print(tupla)

# tupla.remove(3)
# print(tupla)

# tupla.append(333)
# print(tupla)

# tupla.pop()
# print(tupla)

# ocurrencias = tupla.count(4)
# print(ocurrencias)
