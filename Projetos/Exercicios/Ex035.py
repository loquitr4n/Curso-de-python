# Desenvolva um algoritmo que leia o comprimento de 3 retas e diga ao usuario se elas podem formar
# um triangulo ou nao.
from math import fabs
print('='*40)
print('       ANALISADOR DE TRIÂNGULOS')
print('='*40)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if fabs(b-c) < a < b + c and fabs(a-c) < b < a + c and fabs(c-b) < c < c + b:
    print('Os segmentos acima podem formar um triangulo')
else:
    print('Os segmentos acima NÃO formam um triangulo.')