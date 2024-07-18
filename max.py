lista = [1,3,6,1,87,123,1,32]

# max_lista = max(lista)
# print("numero mas alto es:", max_lista)

aux = lista[0]
for i in lista:
    if i > aux:
        aux = i

print(aux)
