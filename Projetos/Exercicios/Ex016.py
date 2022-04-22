# Crie um programa que leia um numero qualquer pelo teclado e
# mostre sua porção inteira.

from math import floor
num = float(input('Digite um numero: '))
print('O numero {} tem parte inteira {:.0f}'.format(num,floor(num)))
