#LISTA IF/ELSE
#Exercicio 1:
'''
num1 = input("Escreva o 1º numero:\n->")
num2 = input("Escreva o 2º numero:\n->")
while not (num1.isnumeric() and num2.isnumeric()):
    num1 = input("Escreva o 1º numero:\n->")
    num2 = input("Escreva o 2º numero:\n->")

if num1 > num2:
    print(f'o maior numero é o numero {num1}')

else:
    print(f'o maior numero é o numero {num2}')

#Exercicio 2
ano = input('Qual o seu ano de nascimento? \n->')

while not ano.isnumeric():
    ano = input('Qual o seu ano de nascimento? \n->')

ano = int(ano)
if ano <= 2009:
    print('Você pode votar este ano.')

else:
    print('voce nao pode votar este ano.')

#Exercicio 3

senha = input('Digite a senha de acesso:\n->')

while not senha.isnumeric():
    senha = input('Digite a senha de acesso:\n->')

if senha == '1234':
    print('ACESSO PERMITIDO')

else:
    print('ACESSO NEGADO')



#Exercicio 4

maça = input('Quantas maças voce quer comprar?')

preço = 0.25
maça = int(maça)
if maça < 12:
    preço = 0.30
    print(f'voce deve pagar R${preço*maça}')

else:
    print(f'voce deve pagar R${preço*maça}')





#LISTA WHILE
#EXERCICIO 2
nome = input('Diga seu nome: \n->')

while len(nome) <3:
    nome = input('Diga seu nome (deve conter mais de 3 caracteres:) \n->')

idade = int(input('Diga a sua idade: \n->'))
while idade < 0 or idade > 150:
    idade = int(input('Digite uma idade valida: \n->'))

salario = float(input('Digite o seu salario: \n->'))
while salario < 0:
    salario = float(input('Digite um salario valido: \n->'))

sexo = input('Qual o seu sexo? (f/m)')
while sexo!= 'f' and sexo != 'm':
    sexo = input('digite um sexo valido! (f/m)\n->')

es = input('Digite seu estado civil! (s/c/d/v)')
while es != 's' and es != 'c' and es != 'd' and es != 'v':
    es = input('Digite um estado civil valido! (s/c/d/v)\n->')


#EXERCICIO 3

PopA = 80000
PopB=200000
anos = 0
while PopA < PopB:
    PopA += PopA *1.03
    PopB += PopB * 1.015
    anos += 1
print(anos)


usuario = input('Digite seu usuario: \n->')
senha = input('Digite sua senha: \n->')
while senha == usuario:
    senha = input('Digite uma senha diferente do usuario')
print(f'{usuario}\n{senha}')



#EXERCICIO 6

numero = float(input('Digite um número para saber a tabuada: \n->'))
i= 1
while i != 10:
    print(f'{numero} x {i} = {numero * i}')
    i+=1
'''

numero = float(input('Digite um número para saber a tabuada: \n->'))
i= 2
for i in range(1,11):
    print(f'a tabuada de {i}')
for j in range(1,11):
    print(f'{i}+{j} = {i+j}')