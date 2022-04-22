#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa

from time import sleep
menu = 0
maior = 0
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
while not menu == 5:
    menu = int(input('Qual opção você deseja realizar?\n[ 1 ] - SOMAR\n[ 2 ] - MULTIPLICAR\n[ 3 ] - MAIOR\n[ 4 ] - NOVOS NUMEROS\n[ 5 ] - SAIR DO PROGRAMA\n'))
    print(f'OPÇÃO ESCOLHIDA: {menu}')
    if menu == 1:
        soma = num1 + num2
        print('=-' * 40)
        print(f'\033[32mA soma de {num1} + {num2} = {soma}.\033[m')
        print('=-' * 40)
    elif menu == 2:
        mult = num1 * num2
        print('=-' * 40)
        print(f'\033[32mA multiplicação {num1} x {num2} = {mult}.\033[m')
        print('=-' * 40)
    elif menu == 3:
        if num1 > num2:
            maior = num1
            print('=-' * 40)
            print(f'\033[32mO maior numero entre eles é o {maior}.\033[m')
            print('=-' * 40)
        elif num2 > num1:
            maior = num2
            print('=-' * 40)
            print(f'\033[32mO maior numero entre eles é o {maior}.\033[m')
            print('=-' * 40)
        elif num1 == num2:
            print('=-' * 40)
            print('\033[32mOs dois numeros possuem valores iguais.\033[m')
            print('=-' * 40)
    elif menu == 4:
        print('=-' * 40)
        print('\033[32mDigite novos numeros:\033[m')
        print('=-' * 40)
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))
        print('=-' * 40)
    elif menu == 5:
        print('\033[31m=-'*40)
        print('\033[32mFINALIZANDO...')
        sleep(2)
        print('Muito obrigado, volte sempre!!!\033[32m')
        print('\033[31m=-' * 40)
    else:
        print('=-' * 40)
        print('\033[31mOpção invalida, tente novamente.\033[m')
        print('=-' * 40)