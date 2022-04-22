# Exercício Python 081: Crie um programa que vai ler vários números e colocar
# em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista
lista = []
while True:
    lista.append(int(input('Digite um numero:')))
    a = input('Deseja continuar? [S/N]').lower()[0]
    if a == 'n':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} numeros.')
print(f'Os numeros ordenados de forma decrescente são: {lista} ')
if 5 in lista:
    print('O numero 5 está contido na lista.')
else:
    print('O numero 5 não foi encontrado na lista.')