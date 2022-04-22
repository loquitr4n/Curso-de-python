'''Exercício Python 075: Desenvolva um programa que leia quatro valores 
pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

a = (int(input('Digite um numero:')),int(input('Digite um numero:')),int(input('Digite um numero:')),int(input('Digite um numero:')))
b = a
if 3 in b:
    print(f'O primeiro valor 3 foi digitado na {b.index(3)}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print(f'O valor 9 apareceu {b.count(9)} vezes.')
print('Os numero pares digitados foram:', end='')
for n in a:
    if n % 2 == 0:
        print(n, end=' ')

#ou

'''if b[0] % 2 == 0:
    print(f'{b[0]} ', end='')
if b[1] % 2 == 0:
    print(f'{b[1]} ', end='')
if b[2] % 2 == 0:
    print(f'{b[2]} ', end='')
if b[3] % 2 == 0:
    print(f'{b[3]} ', end='')'''
    
# ou:

'''cont = 0
print('Temos os numeros pares: ', end='')
for cont in range(0,4):
    if b[cont] % 2 == 0:
        print(f'{b[cont]}, ', end='')
        cont += 1'''
    