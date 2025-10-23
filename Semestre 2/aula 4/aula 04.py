import matplotlib.pyplot as plt

'''matriz = [[1,2,3,4] , [4,5,6,7], [7,8,9,10]]
plt.imshow(matriz,'hot')
plt.colorbar()
plt.show()

matriz = [[1,2,3,4], [4,5,6,7], [7,8,9,10]]
print(matriz[0])
print(type(matriz[0]))
print(matriz[0][2])
matriz = [[1,2,3,4], [4,5,6,7], [7,8,9,10]]
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")


def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz
def imagem(matriz):
    plt.imshow(matriz, 'hot')
    plt.colorbar()
    plt.show()
    return
def cria_diagonal_ruim(linhas, colunas):
    diagonal = cria_matriz(10,10)
    for i in range(len(diagonal)):
        for j in range(len(diagonal[0])):
            if i == j:
                diagonal[i][i] = 1
    return diagonal
def cria_diagonal_bom(linhas,colunas):
    diagonal = cria_matriz(linhas,colunas)
    for i in range(len(diagonal)):
        diagonal[i][i] = 1
    return diagonal

xadrez = cria_matriz(8,8)
for i in range(len(xadrez)):
    for j in range(len(xadrez[0])):
        if i%2 == 0:
            if j%2 == 0:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1
        else:
            if j%2 == 0:
                xadrez[i][j] = 1
            else:
                xadrez[i][j] = 0
#imagem(xadrez)
circulo = cria_matriz(1000,1000)
raio = len(circulo)/2
for i in range(len(circulo)):
    for j in range(len(circulo[0])):
        if (i-raio)**2 + (j-raio)**2 <= raio ** 2:
            circulo[i][j] = i
        else:
            circulo[i][j] = 0
imagem(circulo)'''


'''def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz


def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)


def diagonal_principal(matriz):
    for i in range(min(len(matriz), len(matriz[0]))):
        matriz[i][i] = 1


def diagonal_secundaria(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        j = colunas - 1 - i
        if 0 <= j < colunas:
            matriz[i][j] = 1


linhas = 10
colunas = 20
matriz = cria_matriz(linhas, colunas)

diagonal_principal(matriz)

mostra_matriz(matriz)


'''
import matplotlib.pyplot as plt

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)

def diagonal_secundaria(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        j = colunas - 1 - i
        if 0 <= j < colunas:
            matriz[i][j] = 1

def mostra_imagem(matriz):
    plt.imshow(matriz)
    plt.colorbar
    plt.show()

linhas = 10
colunas = 10

matriz = cria_matriz(linhas, colunas)
diagonal_secundaria(matriz)

mostra_matriz(matriz)

mostra_imagem(matriz)
