import requests
import pandas as pd

acougue = {
    'Carnes' : ['Patinho','Coxão Mole','Fraldinha','Picanha','Maminha','LINGÜIÇA'],
    'Preço/kg' : [35.90,49.90,39.90,80.00,45.90,15],
    'Estoque' : [10,50,30,15,20,100],
    'Validade' : ['4','7','5','9','20','50']
}
def printa_dic(dic,num=0):
    for key in dic.keys():
        if type(dic[key]) is dict:
            print(key)
            printa_dic(dic[key],num+1)
        else:
            print(f"{num*'  '}{key} : {dic[key]}")
    return



def forca_opcao(msg,lista_opcoes):
    opcoes = '\n'.join(lista_opcoes)
    opcao = input(f"{msg}\n{opcoes}\n->")
    while not opcao in lista_opcoes:
        print("Inválido!")
        opcao = input(f"{msg}\n{opcoes}\n->")
    return opcao

def cria_indices():
    global indices
    indices = {}
    for i in range(len(acougue['Carnes'])):
        indices[acougue['Carnes'][i]] = i
    return indices


def cadastrar():
    global indices
    for key in acougue.keys():
        if 'preço' in key.lower() or 'estoque' in key.lower():
            while True:
                try:
                    info = float(input(f"Diga o novo {key}: "))
                except:
                    print("Tem que ser float")
                else:
                    acougue[key].append(info)
                    break
            continue
        info = input(f"Diga o novo {key}")
        acougue[key].append(info)
    print(acougue)
    indices = cria_indices()
    return

def remover():
    global indices
    item = forca_opcao("Qual item será removido?",acougue['Carnes'])
    indice_item = indices[item]
    for key in acougue.keys():
        acougue[key].pop(indice_item)
    indices = cria_indices()
    return

def atualizar():
    item = forca_opcao("Qual item você deseja atualizar?",acougue['Carnes'])
    indice_item = indices[item]
    keys = list(acougue.keys())
    keys.pop(0)
    for key in keys:
        if forca_opcao(f"Você quer atualizar {key} para {item}?",['sim','não']) == 'sim':
            info = input(f"Diga o novo {key}: ")
            acougue[key][indice_item] = info
    print(pd.DataFrame(acougue))
    return

def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)

def comprar():
    item = forca_opcao("Qual item você quer comprar?",acougue['Carnes'])
    indice_item = indices[item]
    for key in acougue.keys():
        print(f"{key} : {acougue[key][indice_item]}")
    continuar = forca_opcao(f"Você quer levar {item}?",['SIM','não'])
    if continuar == 'não':
        return
    qtd = verifica_numero(f"Quantos kg de {item}?")
    if qtd <= acougue['Estoque'][indice_item]:
        acougue['Estoque'][indice_item] -= qtd
        carrinho['Valor Total'] += qtd*acougue['Preço/kg'][indice_item]
        if item not in carrinho['Itens'].keys():
            carrinho['Itens'][item] = qtd
        else:
            carrinho['Itens'][item] += qtd
    else:
        print(f"Só há {acougue['Estoque'][indice_item]}kg no estoque!")
        comprar()

def cadastro_endereco():
    while True:
        cep = input("Diga seu cep: ")
        endereco = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if endereco.status_code == 200:
            carrinho['Endereço'] = endereco.json()
            carrinho['Endereço']['Nº'] = input("Numero da residencia: ")
            carrinho['Endereço']['Complemento'] = input("Complemento: ")
            break
        else:
            print("Cep Inválido")
    return

def confirmar_compra():
    print("Essas são as infos da sua compra: ")
    printa_dic(carrinho)
    alterar = forca_opcao("Deseja remover algum item?",['s','n'])
    if alterar == 's':
        item = forca_opcao("Qual item vc irá remover?",carrinho['Itens'].keys())
        indice = indices[item]
        qtd = verifica_numero(f"Quantos kg de {item} serão removidos?")
        if qtd <= carrinho['Itens'][item]:
            carrinho['Itens'][item] -= qtd
            carrinho['Valor Total'] -= qtd*acougue['Preço/kg'][indice]
        else:
            print(f"Não é possível remover esse tanto pois só há {carrinho['Itens'][item]}kg")
        confirmar_compra()
    return
indices = cria_indices()
carrinho = {
    "Endereço" : {},
    "Itens" : {},
    "Valor Total": 0
}
acoes = {
    'cadastrar' : cadastrar,
    'remover' : remover,
    'atualizar' : atualizar,
    'sair' : exit
}
print("BEM VINDO À AÇOUGUERIA AGNELLO!!!!👌😘👍🙌😁😒🍖🐏")
usuario = forca_opcao("Você é",['cliente','funcionário'])
if usuario == 'cliente':
    cadastro_endereco()
while True:
    if usuario == 'funcionário':
        operacao = forca_opcao("Qual operação será realizada?",acoes.keys())
        acoes[operacao]()
    else:
        comprar()
        confirmar_compra()
        encerrar = forca_opcao("Encerrar a compra ou ver mais itens?",['encerrar', 'continuar'])
        if encerrar == 'encerrar':
            printa_dic(carrinho)
            break
'''
while True:
    try:
        a = int(input("Diga um numero: "))
        break
    except:
        print('Tente de novo')

while True:
    try:
        a = int(input("Diga um numero: "))
        b = int(input("Diga outro numero: "))
        print(a/b)
    except ValueError:
        print('Digita um numero!!!')
    except ZeroDivisionError:
        print('mano não dá pra dividir por zero')
    except Exception as e:
        print(f"Algo deu errado: {e}")
    else:
        print('Deu certo, continuando...')
        break
a = [5,8,1,7,9,4]
#Peça um numero ao usuario (pode ser i)- interprete esse número como um índice - printe a[i]
while True:
    try:
        i = int(input("Diga um numero: "))
        print(a[i])
        break
    except ValueError:
        print("Deve ser um numero!")
    except IndexError:
        print(f"O número deve estar entre 0 e {len(a) - 1}")
    except Exception as e:
        print('sei la hein')

#Peça um numero inteiro ao usuario, depois peça um float ao usuário. De uma mensagem de erro em cada caso
#possível de erro
while True:
    try:
        mensagem = 'inteiro, nunca texto'
        a = int(input("Diga um numero: "))
        mensagem = 'float (a vírgula é ponto - 1,5 -> 1.5). Nunca texto'
        b = float(input("Diga outro número: "))
        break
    except ValueError:
        print(f"Você deve digitar um número {mensagem}")


def acha_indice(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    raise ValueError(f"Não achei o {elem}")
a = [5,8,1,7,9,4]
#acha_indice(a,10)
#a.index(10)

while True:
    try:
        a = int(input("Diga um numero: "))
        raise Exception
    except ValueError:
        print('erro')
'''