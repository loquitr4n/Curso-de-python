# Escreva um programa que pergunte seu nome todo e responda qual o seu primeiro e ultimo nome.

name = input('Digite seu nome todo: ').split()
print('Seu primeiro nome é {}'.format(name[0]))
print('Seu ultimo nome é {}'.format(name[-1]))