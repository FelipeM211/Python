# 1
saudacoes = {
    'oi': 'olá',
    'tchau': 'falou'
}
resp = input("Diga oi ou tchau: ")
print(saudacoes[resp])

# 2
carros = {
    'nomes': ['celta','up','kombi','uno'],
    'portas': [4,2,6,2],
    'preco': [1000,200,300,100],
    'ano': [2014,2018,1970,2005]
}
carro = input("Digite o nome do carro: ")
for i in range(len(carros['nomes'])):
    if carros['nomes'][i] == carro:
        for key in carros.keys():
            print(f"{key}: {carros[key][i]}")

# 3
maior = max(carros['preco'])
for i in range(len(carros['preco'])):
    if carros['preco'][i] == maior:
        for key in carros.keys():
            print(f"{key}: {carros[key][i]}")

# 4
menor = min(carros['preco'])
for i in range(len(carros['preco'])):
    if carros['preco'][i] == menor:
        for key in carros.keys():
            print(f"{key}: {carros[key][i]}")

# 5
novo = input("Deseja cadastrar um novo carro? (sim/nao): ")
if novo == "sim":
    nome = input("Nome: ")
    portas = input("Portas: ")
    preco = input("Preço: ")
    ano = input("Ano: ")
    carros['nomes'].append(nome)
    carros['portas'].append(int(portas))
    carros['preco'].append(int(preco))
    carros['ano'].append(int(ano))

# 6
remover = input("Deseja remover um carro? (sim/nao): ")
if remover == "sim":
    nome = input("Nome do carro para remover: ")
    for i in range(len(carros['nomes'])):
        if carros['nomes'][i] == nome:
            for key in carros.keys():
                carros[key].pop(i)
            break

# 7
frase = 'O bispo de Constantinopla é um bom desconstantinopolitanizador. Quem o desconstantinopolitanizar, um bom desconstantinopolitanizador será'
frase = frase.lower().replace('.','')
palavras = frase.split(' ')
contador = {}
for palavra in palavras:
    if palavra not in contador.keys():
        contador[palavra] = 1
    else:
        contador[palavra] += 1
print(contador)

# 8
numeros = {
    'zero':'0','um':'1','dois':'2','tres':'3','quatro':'4',
    'cinco':'5','seis':'6','sete':'7','oito':'8','nove':'9'
}
texto = input("Digite uma frase com números por extenso: ")
for key in numeros.keys():
    texto = texto.replace(key,numeros[key])
print(texto)

# 9
d1 = {'a':1,'b':2,'c':3}
d2 = {'b':4,'c':5,'d':6}
comuns = []
for key in d1.keys():
    if key in d2.keys():
        comuns.append(key)
print("Chaves em comum:", comuns)

# 10
nao_comuns = []
for key in d1.keys():
    if key not in d2.keys():
        nao_comuns.append(key)
for key in d2.keys():
    if key not in d1.keys():
        nao_comuns.append(key)
print("Chaves não comuns:", nao_comuns)
