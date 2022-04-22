# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
# em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
print('=-'*25)

print('{:=^50}'.format(' JOGO DA ADIVINHAÇÃO '))

print('=-'*25)
print('Neste jogo o computador vai pensar em um numero aleatório entre 1 e 10.\nVocê será desafiado a acertar em qual numero eu pensei.\nEstá preparado?\nSe sim, vamos la...')
print('=-'*25)
from random import randint
pc = randint(1,10)
cont = 0
tentativa = int(input('Digite um numero: '))
while not tentativa == pc:
    if tentativa != pc:
        cont += 1
    tentativa = int(input('Não foi dessa vez, vamos tentar denovo.\nDigite um numero: '))
    if tentativa == pc:
        print('\033[32mPARABENS, VOCE CONSEGUIU!!!\033[m')
print(f'Foram {cont+1} tentativas no total.')


