# Faça um programa que leia o nome inteiro de uma pessoa e mostre
# > o nome com todas letras maiusculas
# > o nome com todas letras minusculas
# > Quantas letras ao todo( sem considerar espaços)
# > Quantas letras tem o primeiro nome

name = str(input('Digite seu nome todo: ')).strip()
print(name.upper())
print(name.lower())
print('Seu nome ao todo tem {} letras.'.format(len(name) - name.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(name.find(' '))) # ou podemos fazer o seguinte:

separador = name.split()
print('Seu primeiro nome tem {} letras'.format(len(separador[0])))