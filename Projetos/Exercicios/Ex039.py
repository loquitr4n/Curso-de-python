# Faça um programa que leia a data de nascimento de um jovem e informe, de acordo com sua idade:
# Se ELE AINDA VAI SE ALISTAR ao serviço militar.
# Se É A HORA DE ELE SE ALISTAR ao serviço militar.
# Se JA PASSOU DA HORA DE ELE SE ALISTAR ao serviço militar.
# O programa tbm deverá mostrar o tempo que falta ou que passou do prazo.

from math import fabs
from datetime import date

print('=-'*40)
print('                            ALISTAMENTO MILITAR')
print('=-'*40)

'''ano = int(input('Digite seu ano de nascimento: '))

if ano < 2003:
    time = fabs(2003 - ano)
    print('Ja passou {:.0f} ano do ano de seu alistamento! Se ainda nao se alistou corra!'.format(time))
elif ano == 2003:
    print('É a hora de vc se alista!!!')
elif ano > 2003:
    time = ano - 2003
    print('Ainda não é tempo, faltam {} anos para vc se alistar!!!'.format(time))'''

nasc = int(input('Qual ano do seu nascimento? '))
atual = date.today().year
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade < 18:
    print('Sua hora de se alistar ao serviço militar ainda não chegou.')
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o ano de alistamento')
    ano = atual + idade
    print(f'Você irá se alistar em {ano}.')
elif idade == 18:
    print('Você está no ano de alistamento! Procure um posto de alistamento militar o quanto antes.')
else:
    saldo = idade - 18
    print(f'Você ja deveria ter se alistado a {saldo} anos.')
    ano = atual - saldo
    print(f'Seu ano de alistamento foi em {ano}')


