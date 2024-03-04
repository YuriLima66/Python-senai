import requests
import json

cep = str(input('Digite o cep a ser consultado: ').replace('-',''))
res = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
endereco = res.json()

if 'code' in endereco:
    if endereco['code'] == 'invalid':
        print('Por favor digite um cep valido')

    elif endereco ['code'] == 'invalid':
        print(f'O cep {cep} que voce digitou, não foi encontrado')
else:
    print(f'O cep {endereco["cep"]} esta localizado na {endereco["address"]} no bairro {endereco["district"]} em {endereco["city"]} -{endereco["state"]}')