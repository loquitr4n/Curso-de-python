# Faça um programa que leia o sexo de uma pessoa mas só aceite valor "M" ou "F"
# Caso esteja errado, peça a repetição, ate que insiram um valor correto.

sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informação invalida, digite novamente:\nDigite o sexo [M/F]: ')).upper().strip()

print(f'Sexo {sexo} inserido com sucesso!')






