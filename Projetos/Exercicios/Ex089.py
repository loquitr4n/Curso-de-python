'''Exercício Python 089: Crie um programa que leia nome e duas 
notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita 
que o usuário possa mostrar as notas de cada aluno individualmente'''
'''lista = []
notas = []
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    notas.append(nome)
    notas.append(nota_1)
    notas.append(nota_2)
    notas.append(media)
    comando = input('Deseja continuar? [N/S] ').lower()[0]
    lista.append(notas[:])
    notas.clear()
    if comando == 'n':
        break
print('=-'*30)
print('Lista das médias:')
for n in range(0,len(lista)):
    print(f'Nome: {lista[n][0]}  Nota 1: {lista[n][1]}   Nota 2: {lista[n][2]}   Média: {lista[n][3]}')
    print('=-'*30)'''

# Depois de assistir a aula:

lista = []
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media  = (nota_1 + nota_2)/2
    lista.append([nome, [nota_1, nota_2], media])
    comando = input('Deseja continuar? [S/N]').lower()[0]
    if comando == 'n':
        break
print('=-'*30)
print(f'{"No.":<4}{"Nome:":<10}{"Media":>8}')
for i,n in enumerate(lista):
    print(f'{i:<4}{n[0]:<10}{n[2]:>8}')
print('=-'*30)
while True:
    notas = int(input('Mostrar notas de qual aluno(a)? [digite 99 para encerrar]'))
    if notas == 99:
        print('FINALIZANDO...')
        break
    if notas <= len(lista) - 1:
        print(f'As notas do aluno {lista[notas][0]} são {lista[notas][1]}')
    if notas > len(lista):
        print('Comando inexistente, tente novamente.')