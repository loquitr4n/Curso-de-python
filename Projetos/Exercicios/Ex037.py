# Escreva um programa que leia um numero qualquer e peça para o usuario escolher
# qual sera a base de conversão:
# 1 - para binario
# 2 - para octal
# 3 - para hexadecimal

num = int(input('Digite um numero: '))
print('''Escolha uma opção de conversão:
[ 1 ] - Converter para BINARIO
[ 2 ] - Converter para OCTAL
[ 3 ] - Converter para HEXADECIMAL''')
opção = int(input('Escolha uma opção: '))
if opção == 1:
    print('O numero {} convertido para binario é: {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('O numero {} convertido para octal é: {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('O numero {} convertido para hexadecimal é: {}'.format(num,hex(num)[2:]))
else:
    print('Opção invalida, tente novamente.')