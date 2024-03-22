# Exibe uma mensagem inicial para o jogo "JO-KEN-PO"
print("JO-KEN-PO")

# Loop principal do jogo
while True:
    # Solicita a jogada do jogador 1 e converte para minúsculas
    jogador1 = input("Jogador 1, escolha sua jogada: pedra, papel ou tesoura: ").lower()
    # Solicita a jogada do jogador 2 e converte para minúsculas
    jogador2 = input("Jogador 2, escolha sua jogada: pedra, papel ou tesoura: ").lower()

    # Verifica se houve um empate
    if jogador1 == jogador2:
        print("Empate!")
    # Verifica as condições para as vitórias do jogador 1
    elif jogador1 == "pedra":
        if jogador2 == "papel":
            print("Vitória do Jogador 2!") 
        elif jogador2 == "tesoura":
            print("Vitória do Jogador 1!")
        else:
            print("Jogada inválida!")
    elif jogador1 == "papel":
        if jogador2 == "pedra":
            print("Vitória do Jogador 1!") 
        elif jogador2 == "tesoura":
            print("Vitória do Jogador 2!")
        else:
            print("Jogada inválida!")
    elif jogador1 == "tesoura":
        if jogador2 == "papel":
            print("Vitória do Jogador 1!") 
        elif jogador2 == "pedra":
            print("Vitória do Jogador 2!")
        else:
            print("Jogada inválida!")     
    else: 
        print("Jogada inválida!")   

    # Pergunta aos jogadores se desejam jogar novamente
    jogar_novamente = input("Deseja jogar novamente? (sim/não): ").lower()
    # Se a resposta não for "sim", o loop é interrompido e o jogo termina
    if jogar_novamente != "sim":
        print("Obrigado por jogar!")
        break