idade = int(input("Seja bem vindo!\n-Quantos anos você tem?\n->"))
if idade >= 18:
    endereco = input("Qual o seu endereco?\n->")
    vinhos = input("Aqui estão os nossos vinhos da casa:\n-Vinho 1\n-Vinho 2\n-Vinho 3\nQual dos nossos vinhos você deseja comprar?\n->")
    quantidade = int(input("Quantas garrafas deseja comprar?\n->"))
    valor = 40
    if vinhos == "Vinho 1":
        valor = 35
    elif vinhos =="Vinho 2":
        valor = 37
    preco = quantidade * valor
    if preco > 100:
        print(f"O valor da sua compra foi de R${preco}, com frete gratis e será entregue em {endereco}!\n-Obrigado pela preferencia, volte sempre!")
    else:
        frete = 15
        print(f"O valor da sua compra foi de R${preco}!\n-Frete = R$15,00.\n-Valor total: R${preco + frete}!\n-Endereço: {endereco}\n-Obrigado pela preferencia, volte sempre!")
else:
    print("Você não tem idade para comprar bebidas alcoolicas!")