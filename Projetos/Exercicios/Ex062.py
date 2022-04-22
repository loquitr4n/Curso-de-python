#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
termo = t
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += r
        cont += 1
    print('PAUSE')
    mais = int(input('Quantos termos a mais você deseja mostrar? '))
print('FIM')
print(f'Total de termos visualizados: {total}')