'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
print()
dados = {'jogador': str(input('Nome do jogador: '))}
partidas = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))
gols = []
for g in range(0,partidas):
    gols.append(int(input(f'Quantos gols na {g+1}º partida?: ')))
print()
print('=x'*40)
print()
dados['gols'] = gols
dados['total'] = sum(gols)
print(dados)
print()
print('=x'*40)
print()
for k,v in dados.items():
    print(f'O campo {k} tem valor {v}')
print()
print('=x'*40)
print()
print(f'o jogador {dados["jogador"]} jogou {partidas} partidas.')
for i,n in enumerate(gols):
    print(f'=> Na {i+1}º partida fez {gols[i]} gols.')
print(f'Foi um total de {sum(gols)} gols.')