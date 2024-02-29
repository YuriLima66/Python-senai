times = (
    "Palmeiras",
    "Gremio",
    "Atletico-MG",
    "Flamengo",
    "Botafogo",
    "Bragantino",
    "Fluminense",
    "Athletico-PR",
    "Internacional",
    "Fortaleza",
    "Sao Paulo",
    "Cuiaba",
    "Corinthians",
    "Cruzeiro",
    "Vasco",
    "Bahia",
    "Santos",
    "Goias",
    "Coritiba",
    "America-MG"
)#Criando minha times(Dentro da minha tupla) 

pontuacao = (
    70,
    68,
    66,
    66,
    64,
    62,
    56,
    56,
    55,
    54,
    53,
    51,
    50,
    47,
    45,
    44,
    43,
    38,
    30,
    24
)#Criando minha variavel pontuacao

print('-'*40)#Escreva, Criando minha linha trasejada(Parte de cima)
print(f'{"TABELA BRASILEIRÃO":^30}')#Escreva(Formate{Monstre" TABELA BRASILEIRÃO:"centralizado em um campo de 30 caracteres})
print('-'*40)#Escreva, Criando minha linha trasejada(Parte de baixo, exatos 40)

print('\n')#Escreve('\n, Quebre uma linha')


for i in range(0, len(times)):#Este é um loop for que percorre os índices dos elementos na lista times. Ele usa a função range() para gerar uma sequência de números de 0 até o comprimento da lista times.
  print(f'{times[i]:.<30}', end='')#Escreva(formate{mostre, times[i]:.<30}, Argumento end, opcional da função print, especificando que após imprimir o texto, não deve haver nenhum caractere adicional)

  if i < 6:#Compare se i for menor que 6:
    print(f'\033[1;32m{pontuacao[i]}\033[0m Pontos')#Escreva(formate, código de cor,\033[1;32m: Este é um código de escape ANSI que define a cor do texto a ser impresso. No caso, \033[1;32m define a cor verde brilhante.)

  elif i < 12:#Caso i for menor que 12:Verifica multiplas opções
    print(f'\033[1;34m{pontuacao[i]}\033[0m Pontos')#Escreva(formate, código de cor,\033[1;32m: Este é um código de escape ANSI que define a cor do texto a ser impresso. No caso, \033[1;34m define a roxo brilhante.)

  elif i >= 16:#Caso i for maior que 16:Verifica multiplas opções
    print(f'\033[1;31m{pontuacao[i]}\033[0m Pontos')#Escreva(formate, código de cor,\033[1;32m: Este é um código de escape ANSI que define a cor do texto a ser impresso. No caso, \033[1;34m define a vermelho brilhante.)

  else:#Este é o bloco de código que será executado se nenhuma das condições anteriores for satisfeita
    print(f'\033[1;33m{pontuacao[i]}\033[0m Pontos')#Escreva(formate, código de cor,\033[1;32m: Este é um código de escape ANSI que define a cor do texto a ser impresso. No caso, \033[1;34m define a amarelo brilhante.)


print('\n')#Escreve('\n, Quebre uma linha')

print('-'*40)#Escreva, Criando minha linha trasejada(Parte de cima, exatos 40)
print(f'{"G6 do Brasileirão":^30}')
print('-'*40)#Escreva, Criando minha linha trasejada(Parte de baixo, exatos 40)

print('\n')#Escreve('\n, Quebre uma linha')

for i in range(0, len(times)):
  print(f'{times[i]:.<30}', end='')
  print(f'{pontuacao[i]} PONTOS')

  if i == 5:
    break


print('\n')#Escreve('\n, Quebre uma linha')

print('-'*40)#Escreva, Criando minha linha trasejada(Parte de cima, exatos 40)
print(f'{"Z4 do Brasileirão":^30}')
print('-'*40)#Escreva, Criando minha linha trasejada(Parte de baixo, exatos 40)
print('\n')#Escreve('\n, Quebre uma linha')

for i in range(1, len(times)):#loop, variável pega o numero 1 até o comprimento da lista.Intervalo(1, Contar(variavel)):
  print(f'{times[-i]:.<30}', end='')#Escrever(formate'mostrar{variavel "time"[-buscar pontuação do time]})
  print(f'{pontuacao[-i]} PONTOS')#Escreva(formate{mostre"pontuação[i]})

  if i == 4:#Compare se variável i é igual a 4:
    break #pare!

while True:

 consulta = str(input('\nDigite o time ou posição que deseja consultar: ').title())#Variavel = tipo de dados"letras"(digite(quebre a linha\ Digite o time ou posição que deseja consultar).converter para titulo())

 try:#Executando uma exeção
  consulta = int(consulta)#variavel = numero inteiro"converter"(variavel)
  print(f'O time que está na {consulta} posição é {times[consulta-1]}')#Escreva(formate 'O time que está na {mostre"variavel} posição é {mostre"time"[variavel-1]})

 except ValueError:#tratando uma exeção 
  if consulta in times:#Compare variavel "times:"
    print(f'O time {consulta} está na {times.index(consulta)+1} posição')#Escreva(formate'O time {mostre"variavel"}está na {Mostre"endereço atual.variavel(variavel"consulta")+1})

  else:#Este é o bloco de código que será executado se nenhuma das condições anteriores for satisfeita
    print(f'O time {consulta} não participou da competição')#Escreva(formate'O time{mostre "variavel"} não participou da competição)