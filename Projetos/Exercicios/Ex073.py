'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados 
da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

times = ('Palmeiras','Bragantino', 'Atletico-mineiro', 'Fortaleza', 'Atletico-PR', 'Bahia', 'Fluminense',
        'flamengo','Santos', 'Atletico-GO', 'Ceará', 'Corinthians', 'Juventude', 'São paulo', 'Internacional',
        'America-MG', 'Sport', 'Cuiabá', 'Chapecoense', 'Gremio')
print(f'Os 5 primeiros colocados são {times[0:5]}')
print(f'Os ultimos 4 colocados são {times[-4:]}')
print(f'Os time em ordem alfabética: {sorted(times)}')
print(f'A Chapecoense está na {times.index("Chapecoense")+1}° posição.')
