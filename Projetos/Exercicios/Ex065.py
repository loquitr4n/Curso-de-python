#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = ''
cont = soma = maior = menor = 0
while resp != 'N':
    num = int(input('Digite um numero: '))
    cont += 1
    soma += num
    if num > maior:
        maior = num
    elif num < maior:
        menor = num
    resp = input('Deseja continuar? [S/N] ').upper()
print('Você digitou {} numeros e a média entre eles é {}'.format(cont,soma/cont))
print('O maior numero digitado foi {} e o menor foi {}.'.format(maior,menor))

# Outra forma de descobrir o maior e menor numero:
    '''if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num'''
    
