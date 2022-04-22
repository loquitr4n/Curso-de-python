#Exercício Python 078: Faça um programa que leia 5 valores numéricos
# e guarde-os em uma lista. No final, mostre qual 
# foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

num = []
maior = 0
menor = 0
for n in range(0,5):
    num.append(int(input(f'Digite um numero para a {n}ª posição: ')))
print(f'Você digitou os valores: {num}')

print(f'O maior valor digitado foi {max(num)} na posição: ', end='')
for i, v in enumerate(num):
    if v == max(num):
        print(f'{i}...', end='')
        
print()

print(f'O menor valor digitado foi {min(num)} na posição: ', end='')
for i, v in enumerate(num):
    if v == min(num):
        print(f'{i}...', end='')
        