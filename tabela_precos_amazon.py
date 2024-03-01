'''Tabela de preços 
Crie um programa onde vai ter um dicionario com 10 itens que vendem na amazon.
neste dicionario você vai armazenar a quantidade e o valor dos itens.

Você ira mostrar PARA O USUARIO O PRECO DO ITEM E A QUANTIDADE DE ESTOQUE E ELE VAI COMPRANDO E ADIDIONANDO ESSES ITENS AO CARRINHO, ao final, mostre o valor total da compra.'''

amazon = {'alexa':[314.10,235]},{'ps5':[4249.00,200]},{'mochila':[45.88,100]},{'amaciante':[45.88,100]},{'caneta':[2.50,1000]},{'óculos':[78.30,50]},{'funko pop':[150.80,200]}
carrinho = []

while True:
    verificar = str(input('Desejar comprar ou encerrar a compra:[C/E]')).upper()
    if verificar =='C':
        for k,v in amazon.items():
            print(f'\033[1;32m{k:.<30}\033[0m \033[1;31mR${v[0]:<5}\33[0m')

        item = str(input('Qual item você deseja comprar: ')).lower()

        if item in amazon:
            quantidade = int(input('Digite a quantidade: '))
            if amazon[item][1] < quantidade:
                print(f'Quantidade maior que a disponivel, atalmente temos {amazon[item][1]} itens em estoque')
                continue
            amazon[item][1] -= quantidade

            print('nosse estoque atualmente é {amazon[item][1]}')

            valor = amazon[item][0] * quantidade

            carrinho.append(valor)
        else:
            print('produto indisponivel, tente novamente')
            continue
    
    if verificar == 'E':
        break

print(f'Ovalor total da compra foi de \033[1;35m{sum(carrinho):.2f}')
