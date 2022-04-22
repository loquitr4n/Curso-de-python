# Desenvolva um programa que leia seis numero inteiros e mostre a soma
# apenas daqueles que forem pares. se o valor
# digitado for impar, desconsidere-o.

soma = 0
cont = 0
for c in range(1,7):
    num = int(input(f'Digite o N°{c}: '))
    if (num % 2) == 0:
        soma = soma + num
        cont = cont + 1
print('Você digitou {} numeros pares e a soma deles é igual a {}.'.format(cont,soma))



