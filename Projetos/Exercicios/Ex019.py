# Um professor que sortear um de seus 4 alunos para apagar o quadro. Faça um programa que o ajude,
# lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
aluno_1 = (input('Primeiro aluno: '))
aluno_2 = (input('Segundo aluno: '))
aluno_3 = (input('Terceiro aluno: '))
aluno_4 = (input('Quarto aluno: '))
a = [aluno_1, aluno_2, aluno_3, aluno_4]
escolhido = choice(a)
print('O aluno escolhido foi {}'.format(escolhido))