
#1: import do modulo requests
import requests 
import time

#2: formatação do endpoint de acordo com o cep

lista_cep = ['04101300', 
             '01310200', 
             '80530230', 
             '20271130',
             '40026280',
             '95670000',
             '66040170'
             ]

endpoint = 'https://viacep.com.br/ws/{}/json/'

#requisição no endereço 
for cep in lista_cep:

    try:
        resposta = requests.get(endpoint.format(cep))
        resposta.raise_for_status()

    except requests.exceptions.HTTPError as err:
        print('HTTP ERROR - ', err)
    except requests.exceptions.Timeout as err:
        print(err) 
    except requests.exceptions.ConnectionError as err:
        print('erro de conexão - ', err)
    else:
        print(f'status code {resposta.status_code}')
        json = resposta.json()
        print(json)
        print('---------------------------------------')
        time.sleep(1)

# status code == 200


