# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
# retangulo, calcule calcule e mostre o comprimento da hipotenusa.
from math import sqrt
ctt_1 = float(input('Digite um cateto do triangulo retangulo: '))
ctt_2 = float(input('Digite o outro cateto do triangulo: '))
hip = sqrt(ctt_1 ** 2 + ctt_2 ** 2)

print('A hipotenusa do triangulo retangulo cujo catetos medem {} e {}, é: {:.2f} '.format(ctt_1,ctt_2,hip))