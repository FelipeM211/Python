#Felipe Balbino Murad - RM562347

#EX 1
def mostra_matriz(matriz):
    for i in matriz:
        print(i)
    return

#EX 2
def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(1)
        matriz.append(linha)
    return matriz

#matriz = cria_matriz(5,5)
#mostra_matriz(matriz)

#EX 3
def ex3_xadrez(xadrez):
    for i in range(len(xadrez)):
        for j in range(len(xadrez[0])):
            xadrez[i][j] = 1
            if i%2 == j%2:
                xadrez[i][j]= 0
    return matriz

#matriz = cria_matriz(8,8)
#ex3_xadrez(matriz)
#mostra_matriz(matriz)

#EX 4

def ex4_transposta(matriz):
    for i in range(len(i)):
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i]= aux
    return matriz

#matriz([[1,2,3],[4,5,6],[7,8,9]])
#ex4_transposta(matriz)
#mostra_matriz(matriz)

