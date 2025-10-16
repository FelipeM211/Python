lista = [1,2,3,4,5,6,7]

def acha_menor():
    menor = min(lista)
    for i in range(len(lista)):
        if lista[i] == menor:
            for key in carros.keys():
                print(f"{key}: {lista[key][i]}")