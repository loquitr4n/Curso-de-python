# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

print('*-' * 15)
print('     CADASTRE UMA PESSOA')
print('*-' * 15)
cont = cont_h = cont_m = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = input('Sexo: [M/F] ').lower().strip()
        if sexo not in 'mf':
            print('{:=^30}'.format('Opção invalida, tente novamente.'))
    if idade > 18:
        cont += 1
    if sexo == 'm':
        cont_h += 1
    if sexo == 'f' and idade < 20:
        cont_m += 1
    print('*-' * 15)
    proximo = ' '
    while proximo not in 'sn':
        proximo = input('Deseja continuar? [S/N] ').lower().strip()[0]
        if proximo not in 'sn':
            print('{:=^30}'.format('Opção invalida, tente novamente.'))
    print('*-' * 15)
    if proximo == 'n':
        break
print('*-' * 15)
print(f'{cont} pessoas tem mais de 18 anos.')
print(f'{cont_h} homens foram cadastrados.')
print(f'{cont_m} mulheres com menos de 20 anos foram cadastradas.')
print('*-' * 15)
