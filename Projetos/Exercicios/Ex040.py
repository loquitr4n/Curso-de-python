# Escreva um programa que leia duas notas de um aluno, mostre sua media e diga se ele ta aprovado, reprovado
# ou em recuperação.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2

if m < 5:
    print('Voce esta reprovado!')
elif 5 < m < 6.9:
    print('Você está de recuperação!')
elif m >= 7:
    print('Parabens, você esta APROVADO!!!')