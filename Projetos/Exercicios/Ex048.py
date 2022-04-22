# faça um programa que calcule a soma entre todos numeros impares que são multiplos de 3 e que se encontram
# no intervalor de 1 ate 500.

soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todos numeros é igual a {}'.format(soma))


# ou
#print(sum(range(3, 501, 6)))





