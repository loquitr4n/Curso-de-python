#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um numero para saber se é primo: '))
cont = 0
for c in range(1,num+1):
    if num % c == 0:
        print('\033[31m', end='')
        cont += 1
    else:
        print('\033[32m', end='')
    print('{}'.format(c), end=' ')

print('\033[m\nO numero {} foi dividido {} vezes'.format(num,cont))
if cont == 2:
    print('Por isso o numero {} é primo!'.format(num))
elif cont != 2:
    print('Por isso o numero {} NÃO é primo!'.format(num))
