# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com
# valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(*num):
    print('Analisando valores...')
    sleep(0.3)
    cont = mai = 0
    for valor in num:
        print(f'{valor},', end=' ', flush = True)
        sleep(0.2)
        if valor > mai:
            mai = valor
        cont += 1
    print(f'Foram analisado(s) {cont} numero(s).')
    if mai == 0:
        print('O valor zero foi o único digitado')
    print(f'O maior valor inserido foi {mai}.')
    print('-'*30)


maior(3, 4, 2, 6, 0, 9)
maior(9,2,8,7,2,4,10,5,7,2,1)
maior(0)
maior()

