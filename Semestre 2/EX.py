import pandas as pd
import requests

acougue = {
    'Carnes' : ['Patinho', 'Coxão Mole','Fraldinha', 'Picanha', 'Maminha', 'Linguiça'],
    'Preço/kg' : [35.90, 49.90, 39.90, 80, 45.90, 15],
    'estoque' : [10,50,30,15,20,100],
    'Validade' : ['4', '7', '5', '9', '20','50']
}

def cria_indices():
    indices = {}
    for i in range(len(acougue['Carnes'])):
        indices[acougue['Carnes'][i]] = i
    return indices

def forca_opcao(msg, lista_opcoes):
    opcoes = '\n'.join(lista_opcoes)
    opcao = input(f'{msg}\n{opcoes}\n')
    while not opcao in lista_opcoes:
        print('Invalido!')
        opcao = input(f'{msg} \n{opcoes}\n')
    return opcao


def cadastro_endereco():
    while True:
        cep = input('Diga o seu CEP:\n-> ')
        endereco = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if endereco.status_code ==200:
            carrinho['Endereço']= endereco.json()
            carrinho['Endereço']['Nª'] = input('Numero da residencia: \n->')
            carrinho['Endereço']['Complemento'] = input('Complemento: \n ->')

def add_prod():
    global indices
    for key in acougue.keys():
        info = input(f'Diga o novo {key}: ')
        acougue[key].append(info)
    print(pd.DataFrame(acougue))
    indices = cria_indices()
    return

def rem_prod():
    global indices
    item = forca_opcao("Qual carne vc quer remover?", acougue['Carnes'])
    indice_item = indices[item]
    for key in acougue.keys():
        acougue[key].pop(indice_item)
    print(pd.DataFrame(acougue))
    indices = cria_indices()
    return

def atualizar():
    item = forca_opcao('Qual item voce deseja atualizar?\n->',acougue['Carnes'])
    indice_item = indices[item]
    keys = list(acougue.keys())
    keys.pop(0)
    for key in keys:
        if forca_opcao(f'Você quer atualizar {key} para {item}? \n->', ['sim','não']) == 'sim':
            info = input(f'Diga o novo {key}:\n-> ')
            acougue[key][indice_item] = info
    print(pd.DataFrame(acougue))
    return


def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)


def comprar():
    item = forca_opcao('Qual item você quer comprar?\n->', acougue['Carnes'])
    indice_item = indices[item]
    for key in acougue.keys():
        print(f'{key}: {acougue[key][indice_item]}')
    continuar = forca_opcao('Você quer levar?',['sim', 'nao'])
    if continuar == 'nao':
        return
    qtd = verifica_numero(f'Quantos kg de {item}? \n->')
    if qtd <= acougue['estoque'][indice_item]:
        acougue['estoque'][indice_item] -= qtd
        carrinho['Valor Total'] += qtd*acougue['Preço/kg'][indice_item]
        if item not in carrinho['Itens'].keys():
            carrinho['Itens'][item] = qtd
        else:
            carrinho['Itens'][item] += qtd
    else:
        print(f'Só há {acougue['estoque'][indice_item]} kg no estoque!')
        comprar()


indices = cria_indices()
carrinho = {
    'Endereço' : {
        'Rua' : '',
        'Bairro': '',
        'Nª' : '',
        'Cep' : ''
    },
    'Itens' : {},
    'Valor Total' : 0
}
print('Bem vindo à Açougueria Agnelo!!!')
usuario = forca_opcao('Você é',['cliente','funcionario'])
while True:
    if usuario == 'funcionario':
        operacao = forca_opcao('Qual operação será realizada?',['cadastrar','remover','atualizar'])
        if operacao == 'cadastrar':
            add_prod()
        elif operacao == 'remover':
            rem_prod()
        else:
            atualizar()
        continuar = forca_opcao('Você deseja realizar outras operações?',['sim','nao'])
        if continuar == 'nao':
            break
        else:
            comprar()
            encerrar = forca_opcao('Encerrar a compra ou ver mais itens?',['encerrar', 'continuar'])
            if encerrar == 'encerrar':
                print(carrinho)
                break


'''for key in carrinho['Endereço'].keys():
    info = input(f'Diga o/z {key}: \n->')
    carrinho['Endereço'][key] = info'''


comprar()
print(carrinho)

'''atualizar()
print('-'*20)
add_prod()
print('-'*20)
rem_prod()
print('-'*20)
print(pd.DataFrame(acougue))'''