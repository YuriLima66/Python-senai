import requests
import json
while True:

    cep = str(input('Digite o cep a ser consultado: ').replace('-',''))
    res = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
    endereco = res.json()

    if 'code' in endereco:
        if endereco['code'] == 'invalid':
            print(f'O cep {cep} que voce digitou, não foi encontrado, por favor digite um cep valido:')
            
    else:
        print(f'O cep {endereco["cep"]} esta localizado na {endereco["address"]} no bairro {endereco["district"]} em {endereco["city"]} -{endereco["state"]}')
        break
    