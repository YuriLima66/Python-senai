import requests

# Função para converter moeda
def converter_moeda(valor, moeda_origem, moeda_destino, api_key):
    # URL da API para obter as taxas de câmbio
    url = f"https://open.er-api.com/v6/latest/{moeda_origem}"
    # Cabeçalhos da requisição HTTP com a chave de autenticação
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    # Fazendo a requisição GET para obter as taxas de câmbio
    response = requests.get(url, headers=headers)
    
    # Verificando se a requisição foi bem sucedida
    if response.status_code == 200:
        # Convertendo a resposta para JSON
        data = response.json()
        # Obtendo a taxa de câmbio para a moeda de destino
        taxa_cambio = data['rates'].get(moeda_destino)
        # Verificando se a moeda de destino é suportada
        if taxa_cambio:
            # Calculando o valor convertido
            valor_convertido = valor * taxa_cambio
            return valor_convertido
        else:
            return f"A moeda de destino '{moeda_destino}' não é suportada."
    else:
        return "Falha ao obter as taxas de câmbio."

# Insira sua chave de API aqui
api_key = "sua_chave_de_api_aqui"

# Solicita ao usuário que insira o valor, a moeda de origem e a moeda de destino
valor = float(input("Digite o valor a ser convertido: "))
moeda_origem = input("Digite a moeda de origem (por exemplo, USD): ").upper()
moeda_destino = input("Digite a moeda de destino (por exemplo, EUR): ").upper()

# Chama a função converter_moeda com os parâmetros fornecidos
resultado = converter_moeda(valor, moeda_origem, moeda_destino, api_key)

# Verifica se o resultado é um número (ou seja, a conversão foi bem sucedida)
if isinstance(resultado, float):
    # Imprime o resultado da conversão
    print(f"{valor:.2f} {moeda_origem} equivale a {resultado:.2f} {moeda_destino}")
else:
    # Imprime uma mensagem de erro, caso contrário
    print(resultado)
