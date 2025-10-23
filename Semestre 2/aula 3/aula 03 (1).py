import matplotlib.pyplot as plt
'''matriz = [[1,2,3,4] , [4,5,6,7] , [7,8,9,10]]
plt.imshow(matriz,'hot')
plt.colorbar()
plt.show()

matriz = [[1,2,3,4] , [4,5,6,7] , [7,8,9,10]]
print(matriz[0])
print(type(matriz[0]))
print(matriz[0][2])

matriz = [[1,2,3,4] , [4,5,6,7] , [7,8,9,10]]
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(f'matriz[{i}][{j}] = {matriz[i][j]}')'''


linhas = 3
colunas = 4


def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
def fazer_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            if (i%2 == False and j%2 == True) or (i%2 == True and j%2 == False):
                linha.append(1)
            else:
                linha.append(0)
        matriz.append(linha)
    return matriz

a = fazer_matriz(6,6)
mostra_matriz(a)
plt.imshow(a,'hot')
plt.colorbar()
plt.show()

circulo = fazer_matriz(100,100)
raio = len(circulo)/2
for i in range(len(circulo)):
    for j in range(len(circulo[0])):
        if i**2 + j**2 <= raio ** 2:
            circulo[i][j] = 1
        else:
            circulo[i][j] = 0
Imagem(circulo)
plt.imshow(a,'hot')
plt.colorbar()
plt.show()