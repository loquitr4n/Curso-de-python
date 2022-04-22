'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

print('-='*50)
lista = list()
dados = list()
mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(lista) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    lista.append(dados[:])
    conf = input('Deseja continuar?[S/N] ').upper()[0]
    dados.clear()
    if conf == 'N':
        break
print()
print('-='*50)
print()
print(f'Foram cadastradas {len(lista)} pessoas!')
print('Os maiores pesos foram de(a): ',end='')
for p in lista:
    if p[1] == mai:
        print(f'[{p[0]}] ',end='')
print()
print('Os menores pesos foram de(a): ',end='')
for p in lista:
    if p[1] == men:
        print(f'[{p[0]}] ',end='')
print()
print('-='*50)
