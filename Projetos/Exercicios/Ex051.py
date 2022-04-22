# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

t = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão da PA? '))
for c in range(t,100000,r)[:10]:
    print(c, end=' → ')
print('Acabou')

