# Crie um algoritmo que leia tres numeros e mostre na tela qual é o maior e qual é o menor.

a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))

#Forma mais dificil de fazer:
'''if a < b and a < c:
   # print('O menor valor digitado é: {}'.format(a))
if a > b and a > c:
    print('O maior valor digitado foi: {}'.format(a))
if b > a and b > c:
    print('O maior valor digitado foi: {}'.format(b))
if b < a and b < c:
    print('O menor valor digitado é: {}'.format(b))
if c < b and c < a:
    print('O menor valor digitado é: {}'.format(c))
if c > a and c > b:
    print('O maior valor digitado foi: {}'.format(c))'''

# Forma mais facil:

# Verificando o menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando o maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior valor digitado foi {}.'.format(maior))
print('O menor valor digitado foi {}.'.format(menor))
