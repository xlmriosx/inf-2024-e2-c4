# Al pasarle una tupla a la funcion, debe devolver una lista
# Restricciones, no usar la funcion list()
# def to_list(tupla):
#     # Codigo aqui
#     return lista

def to_list(tupla):
    if type(tupla) == type((1,2,3)):
        lista=[]
        for x in range(0,len(tupla)):
            lista.append(tupla[x])
        return lista
    else:
        print('No se puede realizar la operacion debido a que no es una tupla')
        return None
    
# def suma(a, b):
#     return a + b
# suma = lambda a, b: a + b
# print(suma(5,15))

# Algoritmos de ordenamiento
def seleccion(lista_desordenada):
    return lista_ordenada

def insercion(lista_desordenada):
    return lista_ordenada

def intercambio(lista_desordenada): # burbuja
    return lista_ordenada