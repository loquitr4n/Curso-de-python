# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o
# nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
# algum dado não tenha sido informado corretamente.


def atleta(a='', b=''):
    if a != '' and b != '':
        print(f'O jogador {a} fez {b} gol(s) no campeonato.')
    elif a == '' and b == '':
        print(f'O jogador <desconhecido> fez 0 gol(s) no campeonato.')
    elif a == '' and b != '':
        print(f'O jogador <desconhecido> fez {b} gol(s) no campeonato.')
    elif a != '' and b == '':
        print(f'O jogador {a} fez 0 gol(s) nesse campeonato.')


# Programa principal:

jogador = str(input('Nome do jogador: '))  # Nome do jogador
n_gols = (input('Numero de gols: '))  # Numero de gols do jogador
atleta(jogador, str(n_gols))

# Resolução do professor


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = int(input('Numero de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)



