#Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = []
somcol = []
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}][{c}]: '))        
print(40*'-=')
print()

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma.append(matriz[l][c])
        
    print()

for l in range(0,3):
    somcol.append(matriz[l][2])


print(f'\nA soma dos valores pares da matriz é {sum(soma)}.')
print(f'A soma do valores da terceira coluna é: {sum(somcol)}')
print(f'O maior valor da segunda linha é o {max(matriz[1])}')