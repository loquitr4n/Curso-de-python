#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
cont = 0

for c in range(1,8):
    data = int(input(f'Informe o ano de nascimento da {c}° pessoa: '))
    if atual - data < 21:
        cont += 1
print(f'{cont} pessoas ja atingiram a maioridade e {c-cont} pessoas ainda nao atingiram a maioridade.')