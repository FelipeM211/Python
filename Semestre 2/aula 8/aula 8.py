def indice_menor(lista):
    indice = 0
    for i in range(len(lista)):
        if lista[i] < lista[indice]:
            indice = i
    return indice

def selection_sort(lista):
    ordenada = []
    while lista:
        ind = indice_menor(lista)
        menor = lista.pop(ind)
        ordenada.append(menor)
    return ordenada


def selection_sort_melhorzinho(lista):
    for i in range(len(lista)):
        ind = indice_menor(lista[i:]) + i
        aux = lista[i]
        lista[i] = lista[ind]
        lista[ind] = aux
    return lista


lista = [5, 0, 4, 1, 2, 7, 6, 3]
selection_sort_melhorzinho(lista)
print(lista)
