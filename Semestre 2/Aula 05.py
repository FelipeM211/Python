'''dic = {'chave' : 'valor'}
print(dic['chave'])
dic['nova chave'] = 'novo valor'
print(dic)
dic['chave'] = '123'
print(dic)
import random

saudacoes = {
    'oi':['Olá','SALVE','iae','BÃO uai'],
    'tchau':['flw','tchau migo','bjsssss diva','até mais']
}
while True:
    resposta = input("Diga oi ou tchau: ")
    print(random.choice(saudacoes[resposta]))

if resposta == 'oi':
    print('Olá')
else:
    print('flw')

poligonos = {
    '3' : 'Triângulo',
    '4' : 'Quadrado',
    '5' : 'Pentágono',
    '6' : 'Hexágono'
}
resposta = input("Diga a qtd de lados do seu polígono: ")
print(f"Você escolheu um {poligonos[resposta]}")

emojis = {
    ':)' : '😊',
    ':(' : '😒',
    '<3' : '❤️',
    ":'(" : '😢'
}
texto = 'eu amo python <3'
for key in emojis.keys():
    texto = texto.replace(key,emojis[key])
print(texto)

numeros = {
    'zero' : '0',
    'um' : '1',
    'dois' : '2',
    'tres' : '3',
    'quatro' : '4',
    'cinco' : '5',
    'seis' : '6',
    'sete' : '7',
    'oito' : '8',
    'nove' : '9'
}
telefone = input("Diga seu telefone: ")
for key in numeros.keys():
    telefone = telefone.replace(key,numeros[key])
print(telefone)
telefone = telefone.replace(' ','')
print(f"O número de telefone é {telefone}")

dic = {
    'nome' : ['danilo','Bernardo','Matheus'],
    'idade' : [20,18,19]
}
for i in range(len(dic['nome'])):
    for key in dic.keys():
        print(f"{key} : {dic[key][i]}")
    print()
'''



frase = "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."
print(frase)
frase = frase.lower()
print(frase)
frase = frase.replace('.','')
print(frase)
palavras = frase.split(' ')
print(palavras)
contador = {}
for palavra in palavras:
    if palavra not in contador.keys():
        contador[palavra] = 1
    else:
        contador[palavra] += 1
    print(contador)















