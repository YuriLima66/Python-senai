import random
import string

# Função para gerar senha
def gerar_senha(tamanho):
    # Define os caracteres que podem ser usados na senha
    caracteres = string.ascii_letters + string.digits + "!@#?" * 2
    # Gera a senha aleatoriamente usando os caracteres definidos
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Loop principal para gerar senhas
while True:
    # Solicita ao usuário que insira o tamanho da senha desejada
    tamanho_senha = int(input("Digite a quantidade de caracteres que deseja: "))
    # Chama a função para gerar a senha com o tamanho fornecido
    senha_gerada = gerar_senha(tamanho_senha)
    # Exibe a senha gerada
    print("A senha gerada é:", senha_gerada)

    # Solicita ao usuário se deseja refazer a senha
    opcao = input("Deseja refazer a senha? (S/N): ")
    # Verifica a escolha do usuário
    if opcao.lower() == 'n':
        # Se o usuário digitar 'n', sai do loop
        break
