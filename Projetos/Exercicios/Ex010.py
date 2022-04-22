# Crie um programa que leia quando de dinheiro uma pessoa tem na carteira
# e mostre quantos dolares ela pode comprar. Considere U$1,00 = R$3,27

carteira = int(input('Quantos reais tem na sua carteira? '))

a = carteira/3,27

print('Com o seu dinheiro da pra comprar {} dólares.'.format(a))