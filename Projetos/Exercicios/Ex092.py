'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e
carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime
tudo = []
dados = dict()

dados['Nome'] = str(input('Nome:'))
nasc = int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('CTPS: [0 se nao tiver] '))
dados['idade'] = datetime.now().year - nasc
if dados['CTPS'] != 0:
    dados['Ano de contratacao'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salario: '))
    dados['Aposentadoria'] = (dados['Ano de contratacao'] + 35) - nasc

tudo.append(dados.copy())
print()
print(f'{"RESULTADO":=^50}')
print()
for k,v in dados.items():
    print(f'{k} tem o valor: {v}')