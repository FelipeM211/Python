'''# 1
saudacoes = {
    'oi': 'olá',
    'tchau': 'falou'
}
resp = input("Diga oi ou tchau: ")
print(saudacoes[resp])

# 2'''
carros = {
    'nomes': ['celta','up','kombi','uno'],
    'portas': [4,2,6,2],
    'preco': [1000,200,300,100],
    'ano': [2014,2018,1970,2005]
}
'''
carro = input("Digite o nome do carro: ")
for i in range(len(carros['nomes'])):
    if carros['nomes'][i] == carro:
        for key in carros.keys():
            print(f"{key}: {carros[key][i]}")

#3 
maior_preco = carros['preco'][0]
indice_maior = 0

for i in range(1, len(carros['preco'])):
    if carros['preco'][i] > maior_preco:
        maior_preco = carros['preco'][i]
        indice_maior = i

print("Carro mais caro:")
for key in carros.keys():
    print(f"{key}: {carros[key][indice_maior]}")
print()

#4 
menor_preco = carros['preco'][0]
indice_menor = 0

for i in range(1, len(carros['preco'])):
    if carros['preco'][i] < menor_preco:
        menor_preco = carros['preco'][i]
        indice_menor = i

print("Carro mais barato:")
for key in carros.keys():
    print(f"{key}: {carros[key][indice_menor]}")
'''
#5
for key in carros.keys():
    info = input(f'Diga o novo {key}: ')
    carros[key].append(info)
print(carros)




