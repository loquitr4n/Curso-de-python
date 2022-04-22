# Aprimoramento da questão 93:

if False:
    lista = []
    cont = 0
    while True:
        dados = {'jogador': str(input('Nome do jogador: '))}
        partidas = int(input(f'Quantas partidas {dados["jogador"]} jogou? '))
        gols = []
        for g in range(0,partidas):
            gols.append(int(input(f'Quantos gols na {g+1}º partida?: ')))
        dados['gols'] = gols
        dados['total'] = sum(gols)
        dados['cod'] = cont = cont + 1
        lista.append(dados)
        stop = str(input('Deseja continuar? [S/N]')).upper()[0]
        if 'N' in stop:
            break
    print('='*40)
    print(f'{"cod":<4}  {"Nome":<10}  {"Gols":<15}  {"Total":<5}')
    print('-'*40)
    for i,j in enumerate(lista):
        print(f'{i+1:<4}  {lista[i]["jogador"]:<10}', end='  ')
        print(f'{str(lista[i]["gols"]):<15}', end='  ')
        print(f'{lista[i]["total"]:<5}')
    print('-'*40)

# Não consegui relacionar o codigo com o nome de cada jogador.

# Código da resolução do professor:

time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('=-'*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 p/ parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Nao existe jogador com codigo {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')