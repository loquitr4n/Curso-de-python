#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120


'''import numpy
lista = []
num = int(input('Digite um numero para saber seu fatorial: '))
for c in range(num-1,-1,-1):
    fat = (num - c)
    lista.append(fat)
    resultado = numpy.prod(lista)
print(f'{num}! = {resultado}')'''

n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! =')
while c > 0:
    print('{} '.format(n), end='')
    print('x' if c > 1 else '=', end='')
    f *= c
    c -= 1
print(f' {f}')







