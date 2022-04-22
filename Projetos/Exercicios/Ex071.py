#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
'''print('='*30)
print('{:^30}'.format(' BANCO BV '))
print('='*30)

valor = int(input('Qual valor deseja sacar: '))
total = valor
ced = 50
total_de_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_de_ced += 1
    else:
        if total_de_ced > 0:
            print(f'Total de {total_de_ced} cedulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_de_ced = 0
        if total == 0:
            break'''

'''print('-'*30)
print('{:^30}' .format(' BANCO ATENA '))
print('-'*30)
d = int(input('Qual valor você quer sacar? R$'))
cont_cinquenta = cont_vinte = cont_dez = cont_um = 0
while True:
    while d - 50 >= 0:
        d -= 50
        cont_cinquenta += 1
    while d - 20 >= 0:
        d -= 20
        cont_vinte += 1
    while d - 10 >= 0:
        d -= 10
        cont_dez += 1
    while d - 1 >= 0:
        d -= 1
        cont_um += 1
    break
if cont_cinquenta != 0:
    print(f'Total de {cont_cinquenta} cedulas de R$50')
if cont_vinte != 0:
    print(f'Total de {cont_vinte} cedulas de R$20')
if cont_dez != 0:
    print(f'Total de {cont_dez} cedulas de R$10')
if cont_um != 0:
    print(f'Total de {cont_um} cedulas de R$1')'''

cedulas = [200, 100, 50, 20, 10, 5, 2, 1]
valor = int(input('Insira o valor que desaja sacar R$ '))
cont = 0
while True:
    if valor >= cedulas[cont]:
        nota = valor // cedulas[cont]
        print(f'Total de {nota} notas de R$ {cedulas[cont]}')
        valor %= cedulas[cont]
    cont += 1
    if valor == 0:
        break
print('\nVolte sempre ao Banco do Cev! Tenha um bom dia!')