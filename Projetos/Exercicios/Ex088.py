# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai
# sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
import time

'''numeros = list(range(1,61))
print('-'*30)
print('      JOGA NA MEGA SENA')
print('-'*30)

jogos = int(input('Quantos jogos quer que eu sorteie? '))
print('-'*30)
print('      SORTEANDO JOGOS...')
print('-'*30)
for c in range(1,jogos+1):
    print(f'\nJogo {c}: ', end='')
    time.sleep(1)
    for n in range(0,6):
        print(f'[{random.choice(numeros)}]',end='')
print()
print('-'*31)
print(' JOGOS SORTEADOS, BOA SORTE!!!')
print('-'*31)'''

#Resolução alternativa:

numeros = list(range(1,61))
lista = []
print('-'*30)
print('      JOGA NA MEGA SENA')
print('-'*30)

jogos = int(input('Quantos jogos quer que eu sorteie? '))
print('-'*30)
print('      SORTEANDO JOGOS...')
print('-'*30)
for c in range(1,jogos+1):
    print(f'\nJogo {c}: ', end='')
    time.sleep(0.5)
    for n in range(0,6):
        lista.clear()
        num = random.choice(numeros)
        if num not in lista:
            lista.append(num)
        print(f'{lista}',end='')
print()
print('-'*31)
print(' JOGOS SORTEADOS, BOA SORTE!!!')
print('-'*31)
