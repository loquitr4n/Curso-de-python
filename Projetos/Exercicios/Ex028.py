# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5
# e peça para o usuario descobrir qual foi o numero escolhido pelo pc.

# O programa deverá escrever na tela se o usuario ganhou ou perdeu.

import random
import time
print('><'*50)
num = int(random.randint(0,5)) # O pc irá fazer uma escolha aleatoria entre 0 e 5
escolha = int(input('Escolha um numero entre 0 e 5: ')) #numero que o usuário deverar escolher
print('><'*50)
print('PROCESSANDO...')
print('><'*50)
time.sleep(2)
if escolha == num:
    print('Voce acertou, parabéns!!!')
else:
    print('Voce errou, eu pensei no numero {} e não no {}.'.format(num,escolha))
print('><'*50)
