amazon = {'alexa': [314.10, 235], 'ps5': [4249.00, 200], 'mochila': [87.60, 300], 'amaciante': [45.88, 100],
          'caneta':[2.50, 1000], 'óculos': [78.30, 50], 'funko pop': [150.80, 200]}
carrinho = []

while True:
  verificar = str(input('Deseja comprar ou encerrar a compra: [C/E] ')).upper()

  if verificar == 'C':
    for k, v in amazon.items():
      print(f'\033[1;32m{k:.<30}\033[0m \033[1;31mR${v[0]:<5}\033[0m')

    item = str(input('Qual item você deseja comprar: ')).lower()

    if item in amazon:
      quantidade = int(input('Digite a quantidade: '))

      if amazon[item][1] < quantidade:
        print(f'Quantidade maior que a disponível, atualmente temos {amazon[item][1]} itens em estoque')
        continue

      amazon[item][1] -= quantidade

      print(f'Nosso estoque de {item} atualmente é {amazon[item][1]}')

      valor = amazon[item][0] * quantidade

      carrinho.append(valor)

    else:
      print('Produto indisponível, Tente novamente')
      continue

  if verificar == 'E':
    break


print(f'O valor total da compra foi de \033[1;35m{sum(carrinho):.2f}'