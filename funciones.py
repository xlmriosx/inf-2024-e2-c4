## CONJUNTO DE ACCIONES EMPAQUETADAS
# Funciones, f(x) = 2.x = Resultado
# Procedimiento, f(x) = 2.x = No tengo resultado

def f(x):
    return 2 * x

var_2 = f(2)
var_4 = f(4)

print(var_2)
print(var_4)

# Cohesion: El grado de relacion de los componentes internos
# del codigo. Objetivo: Alto.

# Entrada -> CajaNegra -> Resultado
def caja_negra(lista):
    return sorted(lista)

lista = [3,21,4,56,768,234135,685,53214,23,5,67,8,12]
print(caja_negra(lista))