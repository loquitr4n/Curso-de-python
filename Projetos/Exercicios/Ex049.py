# Repita o exercicio numero 9, fazendo na forma de repetição. tabuada.

# como eu fiz
'''num = int(input('Digite o numero que queira saber a tabuada:'))
cont = 0
for c in range(0,10):
    cont = cont + 1
    print(f'[{num} x {cont}] = {num*cont}')'''


# Como deve ser feito:

num = int(input('Digite o numero que queira saber a tabuada:'))
for c in range(0,11):
    print(f'[{num} x {c}] = {num*c}')
