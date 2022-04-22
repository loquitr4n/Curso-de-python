'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista 
única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''

'''lista = list()
impar = list()
par = list()

for c in range(0,7):
    dig = (int(input('Digite um numero: ')))
    if dig % 2 == 0:
        par.append(dig)
        par.sort()    
    else:
        impar.append(dig)
        impar.sort()      
lista.append(par[:])
lista.append(impar[:])     
print(lista)
'''
# Outra forma de fazer:

num = [[], []]
valor = 0
for n in range(1,8):
    valor = int(input(f'Digite o {n}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('=-' * 30)
num[0].sort()
num[1].sort()
print(f'Os numeros pares são: {num[0]}')
print(f'Os numero impares são {num[1]}')
