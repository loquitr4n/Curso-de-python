'''Exercício Python 091: Crie um programa onde 4 jogadores 
joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.'''


from random import randint
from time import sleep
from operator import itemgetter

ranking = []
jogo = {'Douglas' : randint(1,6), 
        'Jonata' : randint(1,6),
        'Michael' : randint(1,6),
        'Deborah' : randint(1,6)}

for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.7)


ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print()
print(f'{"RANKING DOS GANHADORES":=^40}')
print()

for i, r in enumerate(ranking):
    print(f'{i+1}º lugar: {r[0]} que tirou {r[1]}.')
    sleep(0.7)
