import time
import sys
import random
import string
import math

# 1a) Countdown (linha nova)
def countdown_linha_nova(inicio):
    for i in range(inicio, 0, -1):
        print(i)
        time.sleep(1)
    print("Fim!")

# 1b) Countdown (substituindo a linha)
def countdown_mesma_linha(inicio):
    for i in range(inicio, 0, -1):
        print(f"\r{i}", end="")
        time.sleep(1)
    print("\rFim!")

# 1c) Status de carregamento
def status_carregamento():
    partes = int(input("Em quantas partes dividir 100%? "))
    passo = 100 // partes
    for i in range(0, 101, passo):
        print(f"\rCarregando: {i}%", end="")
        time.sleep(0.3)
    print("\nConcluído")


# 2) Gerador de senhas aleatórias
def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# 3a) Comprimento do círculo
def comprimento_circulo(raio):
    return 2 * math.pi * raio

# 3b) Número de voltas em pista circular
def voltas_pista(raio, distancia):
    comprimento = comprimento_circulo(raio)
    return distancia / comprimento

# countdown_linha_nova(5)
# countdown_mesma_linha(5)
# status_carregamento()
# print(gerar_senha())
# print(comprimento_circulo(50))
# print(voltas_pista(50, 754))



# Calcula o discriminante
def discriminante(a=0, b=0, c=0):
    return b**2 - 4*a*c

# Valida se o Δ é positivo
def delta_positivo(a=0, b=0, c=0):
    return discriminante(a, b, c) > 0

# Calcula as raízes reais (Δ positivo)
import math

def discriminante(a=0, b=0, c=0):
    return b**2 - 4*a*c

def delta_positivo(a=0, b=0, c=0):
    return discriminante(a, b, c) > 0

def raizes_reais(a=0, b=0, c=0):
    if a == 0:
        return "Não é equação do segundo grau"
    delta = discriminante(a, b, c)
    if delta <= 0:
        return "Sem raízes reais"
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2

def bhaskara():
    a = float(input("Digite o valor de a: ") or 0)
    b = float(input("Digite o valor de b: ") or 0)
    c = float(input("Digite o valor de c: ") or 0)

    print(f"Δ = {discriminante(a, b, c)}")

    if delta_positivo(a, b, c):
        x1, x2 = raizes_reais(a, b, c)
        print(f"Raízes reais: x1 = {x1}, x2 = {x2}")
    else:
        print("Sem raízes reais (Δ ≤ 0)")

bhaskara()

