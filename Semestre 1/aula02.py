'''frase = "Hello World"
print (frase)
print("Hello World")

palavra_1 = "olá"
palavra_2 = "Mundo"
print(palavra_1 + " " + palavra_2)
frase = palavra_1 + " " + palavra_2
print(frase)

frase = "Eu"
print(frase)
frase = frase + " " + "sou"
print(frase)
frase = frase + " " + "o"
print(frase)
frase = frase + " " + "Felipe"
print(frase)

frase = input("Diga a primeira frase: ")
print(frase)
frase = frase + " " + input("Diga a segunda palavra: ")
print(frase)
frase = frase + " " + input("Diga a terceira palavra: ")
print(frase)
frase = frase + " " + input("Diga a quarta palavra: ")
print(frase)
frase = frase + " " + input("Diga a quinta palavra: ")
print(frase)

a = 2
b = 3
print(type(a))
soma = a + b
div = a/b
potencia = a**b
sub = a-b
mult = a*b
print(f"A soma entre {a} e {b} é {soma}")
print(f"A soma entre {a} e {b} é {sub}")
print(f"A soma entre {a} e {b} é {div}")
print(f"A soma entre {a} e {b} é {mult}")
print(f"A soma entre {a} e {b} é {potencia}")

nome = input("Diga seu nome: ")
print(f"Olá, {nome}! Bem vindo a calculadora!")
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
soma = a + b
div = a/b
potencia = a**b
sub = a-b
mult = a*b
print(f"A soma entre {a} e {b} é {soma}")
print(f"A subtração entre {a} e {b} é {sub}")
print(f"A divisão entre {a} e {b} é {div}")
print(f"A multiplicação entre {a} e {b} é {mult}")
print(f"A potencia entre {a} e {b} é {potencia}")

a = 3
b = 2
print(f"O resultado de {a} > {b} é {a>b}")
print(f"O resultado de {a} < {b} é {a<b}")
print(f"O resultado de {a} >= {b} é {a>=b}")
print(f"O resultado de {a} <= {b} é {a<=b}")
print(f"O resultado de {a} == {b} é {a==b}")
print(f"O resultado de {a} != {b} é {a!=b}")

a = 2
b = 3
print(f"{a} > {b} and {a} < {b}, ou seja, {2 < 3} and {3 > 2} dá {2 < 3 and 3 > 2}")
print(f"{a} > {b} and {a} > {b}, ou seja, {2 > 3} and {3 > 2} dá {2 > 3 and 3 > 2}")
print(f"{a} < {b} and {a} < {b}, ou seja, {2 < 3} and {3 < 2} dá {2 < 3 and 3 < 2}")
print(f"{a} > {b} and {a} < {b}, ou seja, {2 > 3} and {3 < 2} dá {2 > 3 and 3 < 2}")

a = 2
b = 3
print(f"{a} != {b} or {a} < {b}, ou seja, {2 != 3} or {3 > 2} dá {2 != 3 or 3 > 2}")
print(f"{a} > {b} or {a} < {b}, ou seja, {2 > 3} or {3 > 2} dá {2 > 3 or 3 > 2}")
print(f"{a} < {b} or {a} == {b}, ou seja, {2 < 3} or {3 == 2} dá {2 < 3 or 3 == 2}")
print(f"{a} > {b} or {a} > {b}, ou seja, {2 > 3} or {3 < 2} dá {2 > 3 or 3 < 2}")

idade = int(input("Diga sua idade: "))
if idade >= 18:
    print("aôba😎")
else:
    print("espere até os 18😁")

idoso = input("Você é idoso?\n->")
deficiente = input("Você é deficiente?\n->")
if idoso == 'sim' or deficiente == 'sim' or 's':
    print("Estaciona ae!🚑")
else:
    print("Se para aqui vou conta pra sua mãe🤬😡")'''

idoso = input("Você é idoso?\n->")
deficiente = input("Você é deficiente?\n->")
if idoso == 'sim' or deficiente == 'sim':
    carteirinha = input("Voce tem a carteirinha?\n->")
    if carteirinha == 'sim':
        print("Estaciona ae!🚑")
    else:
        print("Se para aqui vou conta pra sua mãe🤬😡")
else:
    print("Se para aqui vou conta pra sua mãe🤬😡")