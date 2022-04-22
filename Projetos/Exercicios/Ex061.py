#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
termo = t
while cont < 11:
    print(f'{termo} → ', end='')
    termo += r
    cont += 1
print('FIM')