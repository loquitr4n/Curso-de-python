import urllib.request

try:
    site = urllib.request.urlopen('https://www.orkut.com/')
except urllib.error.URLError:
    print('O site Pudim está acessivel.')
else:
    print('Consegui acessar o site Pudim com sucesso.')
