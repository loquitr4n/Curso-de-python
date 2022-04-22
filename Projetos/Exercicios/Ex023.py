# Faça um programa que leia as unidades,dezenas, centenas e milhar de um numero.

num = int(input('Digite um numero: '))
#print('Unidades: {}'.format(num[-1]))
#print('Dezenas: {}'.format(num[-2]))
#print('Centenas: {}'.format((num[-3])))
#print('Milhar: {}'.format(num[-4]))

#ou

#print(f'Unidades: {num[-1]}')
#print(f'Dezenas: {num[-2]}')
#print(f'Centenas: {num[-3]}')
#print(f'Unidade de Milhar: {num[-4]}')
#print(f'Dezenas de milhar: {num[-5]}')

#ou

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidades: {u}')
print(f'Dezenas: {d}')
print(f'Centenas: {c}')
print(f'Milhar: {m}')

