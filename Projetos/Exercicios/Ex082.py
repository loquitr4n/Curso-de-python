#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter
# apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []

while True:
    num = int(input('Digite um numero: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    resp = input('Deseja continuar? [S/N]').lower()[0]
    if resp == 'n':
        break
print(f'Todos numeros digitados: {lista}')
print(f'Os numeros pares da lista são: {par}')
print(f'Os numeros impares da lista são: {impar}')