# Operadores booleans >,<,<=,>=,==,!=
'''a = 2
b = 3
print(f"{a} > {b} and {a} < {b}, ou seja, {2 < 3} and {3 > 2} dá {2 < 3 and 3 > 2}")
idoso = input("Você é idoso?\n->")
carteirinha = input("Você tem a carteirinha?\n->")
if idoso == 'sim' and carteirinha == 'sim':
        print("Estaciona ae!🚑")
else:
    print("Se para aqui vou conta pra sua mãe🤬😡")

idoso = input("Voce é idoso?\n->")
deficiente = input("Voce é deficiente?\n->")
if idoso == "sim" or deficiente == "sim":
    print("Pode estacionar")
else:
    print("Que coisa feia")

letra = input("Escolha uma letra\n->")
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Sua letra é uma vogal")
else:
    print("Sua letra é uma consoante")

time = input("Diga para que time voce torce: ")
if time == "Corinthians":
    print("Maior do brasil")
elif time == "Palmeiras":
    print("Sem mundial, parabens pelo bi da serie B, tia leila faz o pix")
elif time == "São Paulo":
    print("Parabens por ser homossexual")
elif time == "Santos":
    print("Parabens pela serie B, baixa taxa de natalidade, o pele é dahora")

salario = int(input('qual o seu salario: '))
if salario < 1904:
    print("Você não precisa pagar imposto de renda")
elif salario >= 1904 and salario < 2826:
    print(f"Você precisa pagar 7,5% do salario em imposto de renda, ou seja, {salario*0.075} reais.")
elif salario >= 2826 and salario < 3751:
    print(f" Você precisa pagar 15% do salario em imposto de renda, ou seja {salario*0.15} reais.")
elif salario >= 3751 and salario < 4664:
    print(f" Você precisa pagar 22,5% do salario em imposto de renda, ou seja {salario*0.225} reais.")
else:
    print(f" Você precisa pagar 27,7% do salario em imposto de renda, ou seja {salario*0.275} reais.")

nome = input("Qual seu nome?\n->")
entrar = input("Quer fazer contas?\n->")
if entrar == 'sim':
    numero1 = int(input("Digite o primeiro numero: \n->"))
    operacao = input("Qual operação voce quer fazer? \n->")
    numero2 = int(input("Digite o segundo numero: \n->"))
    if operacao == "soma":
        print(f"{nome} a soma de {numero1} + {numero2} é {numero1 + numero2}")
    elif operacao == "subtracao":
        print(f"{nome} a subtracao de {numero1} - {numero2} é {numero1 - numero2}")
    elif operacao == "mutiplicacao":
        print(f"{nome} a multiplicação de {numero1} * {numero2} é {numero1 * numero2}")
    else:
        print(f"{nome} a divisao de {numero1} / {numero2} é {numero1 / numero2}")
else:
    print(f"então vai dormir {nome}")

numero1 = int(input("Digite o primeiro numero:\n->"))
numero2 = int(input("Digite o segundo numero:\n->"))
if numero1>numero2:
    print(f"O maior valor é o {numero1}")
else:
    print(f"O maior valor é o {numero2}")

ano = int(input("Que ano voce nasceu?\n->"))
if ano >= 2009:
    print(f"Voce pode votar já que tem {2025-ano} anos")
else:
    print(f"voce não pode votar ainda, pois so tem {2025-ano} anos")

senha = int(input("Qual a senha\n->"))
if senha == 1234:
    print("ACESSO PERMITIDO😁")
else:
    print("ACESSO NEGADO😡")

quantidade = int(input("Quantas maças voce quer comprar?\n->"))
if quantidade < 12:
    print(f"O valor da compra é R$ {quantidade*0.30}")
elif quantidade >= 12:
    print(f"O valor da compra é R$ {quantidade*0.25}")'''

valor1 = int(input("Qual o primeiro valor?\n->"))
valor2 = int(input("Qual o segundo valor?\n->"))
valor3 = int(input("Qual o terceiro valor?\n->"))
