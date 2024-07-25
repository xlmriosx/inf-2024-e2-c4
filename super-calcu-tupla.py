# Calculadora
# Opciones:
# 1 - Sumar todos los elementos de una lista
# 2 - Encontrar el maximo
# 3 - Encontrar el minimo
# 4 - Filtrar por pares
# 5 - Filtrar por impares
### Ingrese los valores de la lista por pantalla, y ademas la lista puede tener cualquier tamanio
# input()

# lista = []
# condicion = 'si'
# while condicion == 'si':
#     numero = input("Ingresar valor para la lista: ")
#     numero = int(numero)
#     lista.append(numero)
#     condicion = input("Desea seguir cargando valores? (si/no)")

# tupla = tuple(lista)
# print("Su lista cargada es la siguiente:", tupla)

# CRUD => Create Read Update Delete # ABM => Alta Baja Modificacion
tupla = (1,2,3,3,4,5,6,7,8)
opcion = None
while opcion != 0:
    print(f'''
    1 - Sumar todos los elementos de una lista
    2 - Encontrar el maximo
    3 - Encontrar el minimo
    4 - Filtrar por pares
    5 - Filtrar por impares
    6 - Agregar elementos
    7 - Eliminar elementos
    8 - Modificar elementos
    ''')
    opcion = int(input("Por favor ingrese una opcion: "))

    if opcion == 1:
        suma = sum(tupla)
        print(suma)
    elif opcion == 2:
        maximo = max(tupla)
        print(maximo)
    elif opcion == 3:
        minimo = min(tupla)
        print(minimo)
    elif opcion == 4:
        filtradPar = tuple(filter(lambda x: x % 2 == 0, tupla))
        print(filtradPar)
    elif opcion == 5:
        filtradoImpar = tuple(filter(lambda x: x % 2 != 0, tupla))
        print(filtradoImpar)
    elif opcion == 6:
        agregado = list(tupla)
        valor = int(input('Ingrese el valor a agregar a la tupla: '))
        agregado.append(valor)
        agregado = tuple(agregado)
        print(agregado)
    elif opcion == 7:
        eliminado = list(tupla)
        valor = int(input('Ingrese el valor a eliminar de la tupla: '))
        eliminado.remove(valor)
        eliminado = tuple(eliminado)
        print(eliminado)
    elif opcion == 8:
        modificado = list(tupla)

        posicion = int(input('Ingrese posicion a modificar de la tupla: '))
        valor = int(input('Ingrese valor nuevo de la tupla: '))
        modificado[posicion] = valor
        
        modificado = tuple(modificado)
        print(modificado)
    else:
        print('Su opcion ingresada no esta definida dentro de los limites de las opciones.')
