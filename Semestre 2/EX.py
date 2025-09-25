import pandas as pd


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


def add_prod():
    for key in acougue.keys():
        info = input(f'Diga o novo {key}: ')
        acougue[key].append(info)
    print(pd.DataFrame(acougue))
    return

def rem_prod():
    item = forca_opcao("Qual carne vc quer remover?", acougue['Carnes'])
    indice_item = indices[item]
    for key in acougue.keys():
        acougue[key].pop(indice_item)
    print(pd.DataFrame(acougue))
    return

def atualizar():
    item = forca_opcao('Qual item voce deseja atualizar?',acougue['Carnes'])
    indice_item = indices[item]
    keys = list(acougue.keys())
    keys.pop(0)
    for key in keys:
        if forca_opcao(f'Você quer atualizar {key} para {item}? \n->', ['sim','não']) == 'sim':
            info = input(f'Diga o novo {key}:\n-> ')
            acougue[key][indice_item] = info
    print(pd.DataFrame(acougue))
    return


indices = cria_indices()
atualizar()
print('-'*20)
add_prod()
print('-'*20)
rem_prod()
print('-'*20)
print(pd.DataFrame(acougue))