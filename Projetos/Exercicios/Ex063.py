# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma Sequência de Fibonacci.

n = int(input('Digite quantos termo da sequencia deseja visualizar: '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} → {t2}', end='')
while cont <= n:
    t3 = t2 + t1
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' → FIM ', end='')
