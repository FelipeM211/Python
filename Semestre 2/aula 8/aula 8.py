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

def bubble_sort(lista):
    for i in range(len(lista)):
        trocas = 0
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
                trocas += 1
        if trocas == 0:
            break
    return


def busca_binaria(num):
    ini = 0
    fim = num
    while (fim - ini) > 0.001:
        chute = (ini + fim) / 2
        if chute ** 2 > num:
            fim = chute
        else:
            ini = chute
    return chute


def verifica_numero_recursivo(msg):
    num = input(msg)
    while not num.isnumeric():
        num = verifica_numero(msg)
    return int(num)

def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)

def raiz_binaria_recursiva(num,ini =0,fim = 0):
    if fim ==0:
        fim = num
    chute = (ini + fim)/2
    if fim - ini >0.001:
        if chute**2 > num:
            fim = chute
        else:
            ini = chute
        chute = raiz_binaria_recursiva(num,ini,fim)
    return  chute

print(raiz_binaria_recursiva(20))
'''num = verifica_numero_recursivo('Digite um numero \n->')
chute = busca_binaria(num)
print(chute)
'''