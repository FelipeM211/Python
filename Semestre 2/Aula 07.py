def indice_menor(lista):
    indice = 0
    for i in range(len(lista)):
        if lista[i] < lista[indice]:
            indice = i
    return indice


'''def selection_sort(lista):
    ordenada = []
    while lista:
        local_menor = indice_menor(lista)
        menor = lista.pop(local_menor)
        ordenada.append(menor)
    return ordenada
'''


def selection_sort(lista):
    for i in range(len(lista)):
        local_menor = indice_menor(lista[i:]) + i
        aux = lista[i]
        lista[i] = lista[local_menor]
        lista[local_menor] = aux
    return lista


lista = [3, 1, 5, 6, 2, 4, 7]
lista = selection_sort(lista)
print(lista)
