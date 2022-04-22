#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

cont = 0
soma = 0
maior = 0
homem = ''
for p in range(1,5):
    print('{:=^40}'.format(f' {p}° PESSOA '))
    nome = input('Nome: ').lower()
    idade = (int(input('Idade: ')))
    sexo = str(input('Sexo [M,F]: ').lower())
    if idade:
        soma += idade
        media = soma/4
    if idade < 20 and sexo == 'f':
        cont += 1
    if p == 1 and sexo == 'm':
        maior = p
        homem = nome
    if idade > maior and sexo == 'm':
        maior = idade
        homem = nome


print('{:=^40}'.format(' RESULTADO FINAL '))
print(f'{cont} mulheres tem menos de 20 anos de idade.')
print(f'O grupo tem uma média de idade de {media}.')
print(f'O homem de maior idade é de {maior} anos e o seu nome é {homem}.')
print('=-'*50)








