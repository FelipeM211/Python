'''i=0
pares = 0
num = int(input(f"Diga o {i+1}º numero: "))
if num%2 == 0:
    print(f"{num} é par!!!")
    pares = pares + 1
i = i + 1

num = int(input(f"Diga o {i+1}º numero: "))
if num%2 == 0:
    print(f"{num} é par!!!")
    pares = pares + 1
i = i + 1

num = int(input(f"Diga o {i+1}º numero: "))
if num%2 == 0:
    print(f"{num} é par!!!")
    pares = pares + 1
i = i + 1

num = int(input(f"Diga o {i+1}º numero: "))
if num%2 == 0:
    print(f"{num} é par!!!")
    pares = pares + 1
i = i + 1

num = int(input(f"Diga o {i+1}º numero: "))
if num%2 == 0:
    print(f"{num} é par!!!")
    pares = pares + 1
i = i + 1

print(f"Voce digitou {pares} numeros pares e {i - pares} numeros impares.")
i=0
pares=0
while i < 5:
    num = int(input(f"Diga o {i + 1}º numero: "))
    if num%2 == 0:
        pares = pares + 1
    i = i + 1
print(f"Voce digitou {pares} numeros pares e {i - pares} numeros impares.")

senha = '1234'
i = 1
tentativa = input("digite a senha\n->")
while tentativa != senha and i < 3:
    tentativa = input("Senha incorreta!\nTente novamente:\n->")
    i = i + 1
if tentativa == senha:
    print("Acesso liberado")
else:
    print("Acesso Bloqueado!")


sexo = input("Qual o seu sexo?\n-> masculino\n-> feminino\nR: ")
while sexo != 'masculino' and sexo != 'feminino':
    sexo = input("Qual o seu sexo?\n-> masculino\n-> feminino\nR: ")
print("Obrigado!")

sexo = input("Qual o seu sexo?\n-> masculino\n-> feminino\nR: ")
while not (sexo == 'masculino' or sexo == 'feminino'):
    sexo = input("Qual o seu sexo?\n-> masculino\n-> feminino\nR: ")
print("Obrigado!")

codigo = '1234'
senha = input('Digite sua senha numerica:')
while not (senha.isnumeric() == False or senha == codigo):
    senha = input('Digite uma senha valida:')
print('Acesso liberado')'''

#LISTA



