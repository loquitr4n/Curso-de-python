# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria de acordo com a idade.
# ate 9 anos: mirim
# ate 14 anos: infantil
# ate 19 ano: junior
# ate 20 anos: sênior
# acima: master
from datetime import date
ano = int(input('Qual o ano de nascimento do atleta? '))
idade = date.today().year - ano
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 20:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')


