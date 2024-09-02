# while
# numero = 0
# while (numero != 5):
#     print("X:", numero)
#     numero = numero + 1 # numero 4

# for
# for x in range(1, 10):
#     print("el valor de x:", x)

conjuntos = (1,2,3,4,5,6,7,8,9,'123','123','123')
for elemento in conjuntos:
    print(elemento)
    if (elemento == 5):
        print("Estoy utilizando el elemento 5 en este momento")
        break