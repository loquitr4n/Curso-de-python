#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

print('{:=^40}'.format(' LOJA DO DG '))
soma = cont = menor = c = 0
produto = ''
while True:
    produto = (str(input('Digite o nome do produto: ')))
    preço = (float(input('Preço: ')))
    next = ' '
    c += 1
    soma += preço
    if preço >= 1000:
        cont += 1
    if c == 1 or preço < menor:
        menor = preço
        barato = produto
    while next not in 'sn':
        next = str(input('Deseja continuar? [S/N]')).lower()[0]
    if next == 'n':
        break
print(f'O total da compra foi de R${soma} reais.')
print(f'Temos {cont} produto(s) custando mais de R$1000 reais.')
print(f'O produto mais barato foi o(a) {barato} que custa R${menor} reais.')

input('Press enter to continue')

