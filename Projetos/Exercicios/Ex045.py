# Faça um programa que jogue jokenpo.
from time import sleep
from random import randint

for c in range (0,5):
    pc = randint(1,3)
    if pc == 1:
        pc = 'pedra'
    elif pc == 2:
        pc = 'papel'
    elif pc == 3:
        pc = 'tesoura'

    print('=-' * 50)
    minha_jogada = (input('Escolha pedra, papel ou tesoura: ')).lower()
    print('=-'*50)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('POO!!!')
    print('=-'*50)
    if  'pedra' in minha_jogada or 'papel' in minha_jogada or 'tesoura' in minha_jogada:
        if minha_jogada == 'pedra' and pc == 'tesoura' or minha_jogada == 'tesoura' and pc == 'papel' or minha_jogada == 'papel' and pc == 'pedra':
            print('{:=^40}'.format('\033[1;32m VOCÊ GANHOOOOU!!! \033[m'))
            print('=-' * 50)
        elif minha_jogada == pc:
            print('{:=^40}'.format(' Empate!!! '))
            print('=-' * 50)
        else:
            print('{:=^40}'.format(' \033[31mVOCE PERDEU!!!\033[m '))
            print('=-' * 50)
    else:
        print('Opção invalida, tente novamente.')
        print('=-'*50)

    print('Voce escolheu {} e o computador escolheu {}.'.format(minha_jogada,pc))
print('=-'*50)
print('Fim do jogo!!!')
print('=-'*50)
