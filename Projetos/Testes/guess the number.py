# Neste jogo você tentará acertar o numero que o computador pensou.

from random import randint

computer = randint(1, 10)
cont = 0
while True:
    pergunta = int(input('De 1 à 10, qual numero a CPU pensou? '))
    if pergunta == computer:
        print('\033[1;32mParabens, você acertou!!!\033[m')
        break
    else:
        print('\033[1;31mVocê errou, tente novamente.\033[m')
        cont += 1
print(f'Você acertou depois de \033[1;31m{cont}\033[m tentativas.')
