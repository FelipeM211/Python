'''i = 1
while i < 11:
    print(f"Tabuada do {i}:")
    j = 1
    while j < 11:
        print(f"{i}*{j} = {i*j}")
        j+=1
    i+=1
    print()

for i in range(1,11):
    print(f"Tabuada do {i}:")
    for j in range(1,11):
        print(f"{i}*{j} = {i * j}")
    print()

#lista[0] = 3
#lista[1] = 'danilo'
#lista[2] = 0.5
#lista[3] = True

for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")

for elem in lista:
    print(elem)

#Mor cagada
lista = [3,'danilo',0.5,True]
for i in lista:
    print(lista[i])

lista = [3,'danilo',0.5,True]
for elem in lista:
    elem = 1
print(lista)
for i in range(len(lista)):
    lista[i] = 1
print(lista)

lista = [4,1,5,7,3,6,9,2,10,8]
soma = 0
for num in lista:
    soma += num
media = soma/len(lista)

soma = 0
for i in range(len(lista)):
    soma += lista[i]
media = soma/len(lista)

lista = []
print(lista)
lista.append(1)
print(lista)
#Peça 10 numeros ao usuario. Coloque-os dentro da lista. Após a lista estar completa,
#conte a qtd de pares e impares lá dentro.

def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    num = int(num)
    return num
qtd = verifica_numero("Qts numeros voce quer na lista?\n->")
numeros = []

for i in range(qtd): #while len(numeros) < qtd:
    num = verifica_numero(f"Diga o {i+1}º número: ")
    numeros.append(num)

pares = 0
for num in numeros:
    if num%2 == 0:
        pares += 1
impares = len(numeros) - pares
print(f'Na lista {numeros} há {pares} pares e {impares} impares')
'''
def acha_media(lista):
    soma = 0
    for num in lista:
        soma += num
    media = soma/len(lista)
    return media

def local_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            indice_maior = i
            maior = lista[indice_maior]
    return indice_maior

def local_menor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < menor:
            indice_menor = i
            menor = lista[indice_menor]
    return indice_menor

def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    num = int(num)
    return num


def forca_opcao(msg,lista_opcoes,msg_erro = 'Erro'):
    opcoes = ', '.join(lista_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n->")
    while escolha not in lista_opcoes:
        print(msg_erro)
        escolha = input(f"{msg}\n{opcoes}\n->")
    return escolha
def acha_indice(elem,lista):
    for i in range(len(lista)):
        if lista[i] == elem:
           return i
#s_ou_n = ['sim','não']
#continuar = forca_opcao("Você quer continuar? ",s_ou_n)
carros = ['up','gol','polinho turbão manual','uno']
precos = [10,20,1000000,100]
carro = forca_opcao("Qual carro voce quer? ",carros)
indice_carro = acha_indice(carro,carros)
print(f'O carro {carros[indice_carro]} custa R${precos[indice_carro]}')
indice_mais_caro = local_maior(precos)
print(f"O carro mais caro é o {carros[indice_mais_caro]} e custa R${precos[indice_mais_caro]:.2f}")













