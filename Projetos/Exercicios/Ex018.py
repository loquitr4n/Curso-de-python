# Faça um algoritmo que leia um angulo qualquer e mostre na tela
# o valor do seu seno, cosseno e tangente desse angulo.

from math import sin,cos,tan,radians
ang = float(input('Digite um angulo: '))
print('O seno, cosseno e tangente de {} são:'.format(ang))
print('Seno: {:.3f}'.format(sin(radians(ang))))
print('Cosseno: {:.3f}'.format(cos(radians(ang))))
print('Tangente: {:.3f}'.format(tan(radians(ang))))
