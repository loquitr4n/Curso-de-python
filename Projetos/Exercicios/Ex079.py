#Exercício Python 079: Crie um programa onde o usuário possa digitar vários 
# valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
n = lista
cont = 0
while True:
    n = (int(input('Digite um numero:')))
    if n not in lista:
        lista.append(n)
        print('Numero inserido com sucesso!')
    else:
        lista.remove(n)
        print('Numero repetido, nao foi adicionado.')
    cont += 1
    c = input('Deseja continuar? [S/N]').upper()[0]
    if c == 'S':
        continue
    if c == 'N':
        break
    if c != 'NS':
        print('Opção invalida, tente novamente.')
lista.sort()
print('Os numero digitados foram: ', end='')
print(lista, end='')