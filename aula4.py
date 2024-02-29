

def jogo_adivinhacao():
    numero_secreto = 5
    tentativas = 0 

    print("Bem vindo ao jogo de adivinhação! eu escolhi um numero entre 1 e 10, tente adiivinhar!")

    while True:
        tentativa = int(input("Digite o seu palpite:"))
        
        tentativas += 1
        if tentativa < numero_secreto:
            print("tente um numero maior")
        elif tentativa> numero_secreto:
            print("tente um numero menor")
        
        else:
            print(f"Parabens! voce acertou em {tentativas}tentativas")
            break
        

# iniciar jogo 
    jogo_adivinhacao()
