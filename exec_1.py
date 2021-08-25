import requests

import json

# uber
url = 'https://receitaws.com.br/v1/cnpj/17895646000187'
dados = requests.get(url)
print(dados.status_code)
if dados.json().get('status') == 'ERROR':
    print(dados.json().get('message'))
else:
    print('nome:', dados.json().get('nome'))
    print('uf:', dados.json().get('uf'))
    print('telefone:', dados.json().get('telefone'))
    print('email:', dados.json().get('email'))
    print('data de abertura:', dados.json().get('abertura'))
    print('Atividade principal:', dados.json().get(
        'atividade_principal', {})[0].get('text', {}))
    print('Atividades secundárias: ')
    for x in range(0, 8):
        print(dados.json().get('atividades_secundarias')[x].get('text'))
print()
# 99
url = 'https://receitaws.com.br/v1/cnpj/18033552000161'
dados = requests.get(url)
print(dados.status_code)
if dados.json().get('status') == 'ERROR':
    print(dados.json().get('message'))
else:
    print('nome:', dados.json().get('nome'))
    print('uf:', dados.json().get('uf'))
    print('telefone:', dados.json().get('telefone'))
    print('email:', dados.json().get('email'))
    print('data de abertura:', dados.json().get('abertura'))
    print('Atividade principal:', dados.json().get(
        'atividade_principal', {})[0].get('text', {}))
    print('Atividades secundárias: ')
    for x in range(0, 14):
        print(dados.json().get('atividades_secundarias')[x].get('text'))
print()
# terceira
url = 'https://receitaws.com.br/v1/cnpj/1365284000104'
dados = requests.get(url)
print(dados.status_code)
if dados.json().get('status') == 'ERROR':
    print(dados.json().get('message'))
else:
    print('nome:', dados.json().get('nome'))
    print('uf:', dados.json().get('uf'))
    print('telefone:', dados.json().get('telefone'))
    print('email:', dados.json().get('email'))
    print('data de abertura:', dados.json().get('abertura'))
    print('Atividade principal:', dados.json().get(
        'atividade_principal', {})[0].get('text', {}))
    print('Atividades secundárias: ')
    for x in range(0, 8):
        print(dados.json().get('atividades_secundarias')[x].get('text'))
