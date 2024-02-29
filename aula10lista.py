"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os #A Biblioteca OS Python oferece uma vasta gama
#de funcionalidades para interação com o sistema operacional.
#Você pode criar, copiar, renomear e excluir arquivos e pastas,
# além de executar comandos do sistema, gerenciar processos
# e obter informações sobre o sistema.

lista = [] #Criando uma lista vazia

while True:#Enquanto for Verdade
    print('Selecione uma opcao')#Escreva ('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')#variavel = digite('[i]p/inserir, [a]p/apagar, [l]p/listar)

    if opcao == 'i':#Verificando se minha variável foi digitada.
        os.system('cls')#armazenando e limpando meu código
        valor = input('Valor: ')#Armazenando um valor digitado
        lista.append(valor)#Adicionando um item na minha lista
    elif opcao == 'a':#Verificando se minha variável "a" foi digitada(ou seja se existir mais de um aopção).
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:#Para tratar um erro usamos o try
            indice = int(indice_str)#Estou armazenando um numero interio
            del lista[indice]#Estou deletando um numero da minha lista
        except ValueError:#Estou tratando um erro caso o valor não seja o esperado.
            print('Por favor digite número int.')#Escreva ('Digite um numero inteiro')
        except IndexError:#Tratando um erro de Indice_str caso não há
            print('Índice não existe na lista')#Escreva ('Indice não existe na lista')
        except Exception:#Tratando um erro desconhecido 
            print('Erro desconhecido')#Escreva ('Erro desconhecido')
    elif opcao == 'l':#Verificando se minha variável "1" foi digitada(ou seja se existir mais de um aopção).
        os.system('clear')#limpando meu terminal

        if len(lista) == 0:#Comparando e contando minha lista
            print('Nada para listar')#Escreva ('Nada para lista)

        for i, valor in enumerate(lista):#Repetir e enumerar minha lista
            print(i, valor)#Escreva (i, valor)
    else:#Caso for falso
        print('Por favor, escolha i, a ou l.')#Escreva('Por favor, escolha i, a ou l)