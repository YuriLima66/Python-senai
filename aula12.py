from threading import local


dic={'curso':' Python','aula':'aula07','professor':"Fernando"}
print(f'professor {dic["professor"]} que ministra o curso de{dic["curso"]}')

#função clear

dic['aula'] = "aula07 - Dicionarios"
dic.clear()
print(dic)
del dic

#obtendo itens, chaves e valores de um dicionario

carros = {'marca': 'vw', 'modelo':'gol', 'ano_modelo': 2016}
print(f'Itens do dicionarios carros:{carros.items()}')
print(f'Chaves do dicionarios carros:{carros.keys()}')
print(f'Valores do dicionarios carros:{carros.values()}')

#exemplo

'''produtos = { 
    "Mouse": 98.75,
    "Teclado":125.65,
    "Monitor":134.78,
    "Gabinete":170.00,
    "HD Externo":510.50,
    "Headset":125.45,}
while True:
    produto = input("Informe o produto para pesquisar o preço ou fim para sair: ")
    if produto == "fim":
        break
    if produto in produtos:
        print(f"Produto {produto} custa {produtos[produto]}.")
    else:
        print(f"produto  {produto} não encontrado.")'''

#outras funcoes
        dic = {'nome': "fulano", 'sobrenome': 'de tal'}
        local = {'UF':"SP", 'cidade':"São Carlos"}
        dic2 = dic.copy()
        dic.update(local)
        print(len(dic))
        print(f'dic: {dic}')
        print(f'dic2:{dic2}')
 #exemplo 2 
        aluno = {}
        aluno['nome'] = str(input("nome:"))
        aluno['media'] = float(input(f"media de {aluno['nome']}"))
        if aluno['media']>=7:
            aluno['situacao'] = 'Aprovado'
        elif aluno['media']>= 5:
            aluno['situacao'] = 'Recuperação'
        else:
            aluno['situacao']= 'Reprovado'
        print('=='*30)
        for k, v in aluno.items():
            print(f'-{k} é igual a {v}') 