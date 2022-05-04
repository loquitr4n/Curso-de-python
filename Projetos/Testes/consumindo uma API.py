import requests

link_soma_vendas = 'https://minhaapi.douglasfreire.repl.co/pegarvendas'
link_media_vendas = 'https://minhaapi.douglasfreire.repl.co/mediavendas'
try:
    req1 = requests.get(link_soma_vendas)
    dicionario1 = req1.json()
    print(f'{dicionario1["total_vendas"]:.3f}')
except:
    print('Esta API não esta disponivel')

try:
    req2 = requests.get((link_media_vendas))
    dicionario2 = req2.json()
    print(f'{dicionario2["media_vendas"]:.3f}')
except:
    print('Esta API nao esta disponivel.')
