'''import requests
import pandas as pd
import json
with open('data.json','r+') as file:
    groufi = json.load(file)
print(groufi.keys())
def forca_opcao(msg,conjunto_opcoes):
    opcoes = '\n'.join(conjunto_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n->")
    while escolha not in conjunto_opcoes:
        print("Inválido")
        escolha = input(f"{msg}\n{opcoes}\n->")
    return escolha

def cadastrar():
    for key in groufi.keys():
        while True:
            try:
                info = input(f"Diga o novo {key}: ")
                if key == 'Preco':
                    msg = "Deve ser um numero com ponto ao invés de vírgula: 1.000,90 -> 1000.90"
                    info = float(info)
                elif key == 'Estoque':
                    msg = 'Deve ser um número inteiro!'
                    info = int(info)
            except ValueError:
                print(msg)
            else:
                groufi[key].append(info)
                break
    cria_indices()
    return

def cria_indices():
    global indices
    indices = {}
    for i in range(len(groufi['Paradinha'])):
        nome = groufi['Paradinha'][i]
        indices[nome] = i
    return indices

def remover():
    escolha = forca_opcao("Qual item você quer remover?",groufi['Paradinha'])
    indice = indices[escolha]
    for key in groufi.keys():
        groufi[key].pop(indice)
    cria_indices()
    return
def atualizar():
    while True:
        item = forca_opcao("Qual paradinha você vai atualizar?",groufi['Paradinha'])
        indice = indices[item]
        key = forca_opcao(f"Qual info de {item} será alterado?",groufi.keys())
        while True:
            try:
                info = input(f"Diga o novo {key}: ")
                if key in ['Preco',"Dose (mg)"]:
                    msg = "Deve ser um numero com ponto ao invés de vírgula: 1.000,90 -> 1000.90"
                    info = float(info)
                elif key == 'Estoque':
                    msg = 'Deve ser um número inteiro!'
                    info = int(info)

            except ValueError:
                print(msg)
            else:
                groufi[key][indice] = info
                break
        continuar = forca_opcao("Quer alterar mais alguma coisa?",['sim','nao'])
        if continuar == 'nao':
            break

def atualizar_alternativa():
    item = forca_opcao("Qual paradinha você vai atualizar?",groufi['Paradinha'])
    indice = indices[item]
    infos = list(groufi.keys())
    infos.pop(0)
    for key in infos:
        info = input(f"Diga o novo {key} de {item} (enter para ignorar)")
        if info:
            groufi[info][indice] = info

def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        print("Inválido!")
        num = input(msg)
    return int(num)

def comprar():
    print(carrinho)
    opcoes = [paradinha for paradinha in groufi['Paradinha']]
    opcoes.append('sair')
    escolha = forca_opcao("Essas são nossas opções, qual te interessa?",opcoes)
    if escolha == 'sair':
        return
    indice = indices[escolha]
    print(f"Essas são as infos sobre {escolha}:")
    for key in groufi.keys():
        print(f"{key} : {groufi[key][indice]}")
    levar = forca_opcao(f"Vai levar {escolha}?",['sim','não'])
    if levar == 'sim':
        qtd  = verifica_numero(f"Quantos {escolha} ce quer?")
        if qtd > groufi['Estoque'][indice]:
            print("Não temos tudo isso! Voltando ao início!")
        else:
            groufi['Estoque'][indice] -= qtd
            carrinho['Valor Total'] += qtd*groufi['Preco'][indice]
            if escolha in carrinho['Itens'].keys():
                carrinho['Itens'][escolha] += qtd
            else:
                carrinho['Itens'][escolha] = qtd
        comprar()
def get_endereco():
    while True:
        cep = input("Diga seu cep: ")
        endereco = f'https://viacep.com.br/ws/{cep}/json/'
        endereco = requests.get(endereco)
        if endereco.status_code == 200:
            endereco = endereco.json()
            carrinho['Endereço'] = endereco
            carrinho['Endereço']['Nº'] = input("Nº: ")
            carrinho['Endereço']['Complemento'] = input("Complemento: ")
            print(carrinho['Endereço'])
            return
        else:
            print("Cep Inválido!")

def confirma_compra():
    print(f"Estas são suas compras: {carrinho['Itens']}")
    retirar = forca_opcao("Deseja remover algo?",['sim','nao'])
    if retirar == 'nao':
        return
    item = forca_opcao("Qual item?",carrinho['Itens'].keys())
    indice = indices[item]
    qtd = verifica_numero(f"Quantos {item} você quer remover?")
    if qtd < carrinho['Itens'][item]:
        restante = carrinho['Itens'][item] - qtd
        carrinho['Valor Total'] -= carrinho['Itens'][item]*groufi['Preco'][indice]
        carrinho['Valor Total'] += restante*groufi['Preco'][indice]
        carrinho['Itens'][item] -= qtd
    else:
        print(f"Não tem tudo isso de {item} no seu carrinho!")
    encerrar = forca_opcao("Podemos encerrar a compra?",['sim','não'])
    if encerrar == 'sim':
        return
    confirma_compra()

indices = cria_indices()
carrinho = {
    'Endereço' : {},
    'Itens' : {},
    'Valor Total' : 0
}
acoes = {
    'atualizar' : atualizar,
    'remover' : remover,
    'cadastrar' : cadastrar
}
perfil = forca_opcao("Você é cliente ou funcionario?",['cliente','funcionario'])
if perfil == 'cliente':
    get_endereco()
    comprar()
    confirma_compra()
    print(carrinho)
else:
    acao = forca_opcao("O que você fará?",acoes.keys())
    acoes[acao]()
    print(pd.DataFrame(groufi))
    file.close()
with open("data.json",'w') as file:
    json.dump(groufi,file,indent = 4)
file.close()


def indice_menor(lista):
    indice = 0
    for i in range(len(lista)):
        if lista[i] < lista[indice]:
            indice = i
    return indice

def selection_sort(lista):
    ordenada = []
    for i in range(len(lista)):
        local_menor = indice_menor(lista)
        menor = lista.pop(local_menor)
        ordenada.append(menor)
    return ordenada

def selection_sort_melhorzinho(lista):
    for i in range(len(lista)):
        local_menor = indice_menor(lista[i:]) + i
        aux = lista[i]
        lista[i] = lista[local_menor]
        lista[local_menor] = aux
        print(lista)
    return

def bubble_sort(lista):
    j = 0
    while True:
        trocas = 0
        for i in range(len(lista)-1-j):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                trocas += 1
        j += 1
        if trocas == 0:
            return

def raiz_binaria(num):
    ini = 0
    fim = num
    sinal = '>'
    while fim - ini > 0.001:
        chute = (ini+fim)/2
        print(f"chute: {chute} -> {chute**2}{sinal}{num}, precisao atual: {fim - ini}")
        if chute**2 > num:
            fim = chute
            sinal = '>'
        else:
            ini = chute
            sinal = '<'
    return chute
print(raiz_binaria(25))

