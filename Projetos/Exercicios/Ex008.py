# Escreva um programa que leia um valor em metros  e o exiba convertido em
# centimetros e milimetros.

numero = int(input('Digite um numero: '))

n_centimetro = numero*100
n_milimetro = numero*1000

print('O valor informado em centimetros é {}, e em milimetros é {}'.format(n_centimetro,n_milimetro))