def indice_menor(lista):
    indice = 0
    for i in range(len(lista)):
        if lista[i] < lista[indice]:
            indice = i
    return indice

def selection_sort(lista):
    ordenada = []
    qtd = len(lista)
    for i in range(qtd):
        local_menor = indice_menor(lista)
        menor = lista.pop(local_menor)
        ordenada.append(menor)
    return ordenada

def selection_sort_menos_ruim(lista):
    for i in range(len(lista)):
        localmenor = indice_menor(lista[i:]) + i
        aux = lista[i]
        lista[i] = lista[localmenor]
        lista[localmenor] = aux
        print(lista)
    return

lista = [3,1,5,6,2,4,7]