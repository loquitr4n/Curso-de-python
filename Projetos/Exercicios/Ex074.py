'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e 
colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também 
indique o menor e o maior valor que estão na tupla'''

from random import randint,sample
num = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
num_sorted = sorted(num)
print(f'Os numero sorteados foram: {sorted(num)}')
print(f'O maior valor randomizado foi {num_sorted[-1]}')
print(f'O menor valor randomizado foi {num_sorted[0]}')
