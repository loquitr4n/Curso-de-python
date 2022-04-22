# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
# somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre # todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


def sorte():
    print('Sorteando 5 numeros: ', end='', flush=True)
    lista = []
    for n in range(0, 5):
        a = randint(0, 10)
        sleep(0.3)
        print(f'{a} ', end='')
        lista.append(a)
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    print(f'\nSomando os valores pares da {lista}, temos {sum(pares)}')


# Programa principal:

sorte()

# Codigo do professor:


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('<< PRONTO!!! >>')


def SomaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da {lista}, temos {soma}.')


# Programa principal


num = list()
sorteia(num)
SomaPar(num)
