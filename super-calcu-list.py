# Calculadora
# Opciones:
# 1 - Sumar todos los elementos de una lista
# 2 - Encontrar el maximo
# 3 - Encontrar el minimo
# 4 - Filtrar por pares
# 5 - Filtrar por impares
### Ingrese los valores de la lista por pantalla, y ademas la lista puede tener cualquier tamanio
# input()

lista = [32,1,2,3,4,5,65]
condicion = 'si'
# while condicion == 'si':
#     numero = input("Ingresar valor para la lista: ")
#     numero = int(numero)
#     lista.append(numero)
#     condicion = input("Desea seguir cargando valores? (si/no)")

print("Su lista cargada es la siguiente:", lista)

opcion = None
while opcion != 0:
    print(f'''
    1 - Sumar todos los elementos de una lista
    2 - Encontrar el maximo
    3 - Encontrar el minimo
    4 - Filtrar por pares
    5 - Filtrar por impares
    ''')
    opcion = int(input("Por favor ingrese una opcion: "))

    if opcion == 1:
        suma = sum(lista)
        print(suma)
    elif opcion == 2:
        maximo = max(lista)
        print(maximo)
    elif opcion == 3:
        minimo = min(lista)
        print(minimo)
    elif opcion == 4:
        filtradPar = list(filter(lambda x: x % 2 == 0, lista))
        print(filtradPar)
    elif opcion == 5:
        filtradoImpar = list(filter(lambda x: x % 2 != 0, lista))
        print(filtradoImpar)
    else:
        print('Su opcion ingresada no esta definida dentro de los limites de las opciones.')
