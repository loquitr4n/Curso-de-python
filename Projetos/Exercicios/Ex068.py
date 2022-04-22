#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint
print('*-'*30)
dedos = int(input('Quantos dedos deseja colocar? ')) # Quantos dedos irei colocar
decisão = input('Par ou impar? [P/I] ').upper() # Minha decisão de par ou impar
resultado = '' # Resultado final
cont = 0 # Contador
print('*-'*30)
while True:
    pc = randint(0, 10) # Numero que o PC irá randomizar
    soma = pc + dedos # Soma dos dedos eu + pc
    if soma % 2 == 0: # se o total for par...
        resultado = 'PAR'
        print(f'Você jogou {dedos} e o pc {pc}, gerando um total de {soma}. Deu {resultado}.')
        if resultado == decisão:
            print('*-' * 30)
            print('VOCE GANHOU!!!')
            print('*-' * 30)
        else:
            print(f'GAME OVER!!! Você ganhou {cont} vezes.')
            break
    elif soma % 2 != 0: # se o resultado for impar...
        resultado = 'IMPAR'
        print(f'Você jogou {dedos} e o pc {pc}, gerando um total de {soma}. Deu {resultado}.')
        if resultado == decisão:
            print('*-' * 30)
            print('VOCE GANHOU!!!')
            print('*-' * 30)
        else:
            print('*-' * 30)
            print(f'GAME OVER!!! Você ganhou {cont} vezes.')
            print('*-' * 30)
            break
    cont += 1
    dedos = int(input('Quantos dedos deseja colocar? '))
    decisão = input('Par ou impar? [P/I] ').upper()






