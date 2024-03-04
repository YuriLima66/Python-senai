[]
import random as rd
from time import sleep
from operator import itemgetter

jogadores = {}
ganhador = 0

for i in range(6):
 
    nome_jogador = str(input('Digite o nome do jogador: ')).strip().title() 
    
    # adicionar while com condição para o nome nao repetir

    jogadores[nome_jogador] = rd.randint(1,10)
    jogador  = (jogadores[nome_jogador])
    if jogador > ganhador:
        ganhador = (jogadores[nome_jogador])
        nome_ganhador = (nome_jogador)
    print('Jogando o dado... ')
    #sleep(0.5)
    

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)


for indice, valor in enumerate(ranking):
    print(f'O {valor[0]} tirou {valor[1]}')

print(f'O ganhador do jogo é o {nome_ganhador} com {ganhador} pontos')