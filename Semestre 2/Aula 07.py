lista = [5,6,2,3,4]


def indice_menor(lista):
    indice = 0
    for i in range(len(lista)):
        if lista[i] < lista[indice]:
            indice = i
    return indice


def selection_sort(lista):
    aux = 0
    while lista:
        local_menor = indice_menor(lista)
        menor = lista.pop(local_menor)
        ordenada.append(menor)
    return ordenada

print(lista)
ordenada = selection_sort(lista)
print(ordenada)
