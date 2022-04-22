#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media do(a) {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print()
print('=-'*30)
print(f'Nome do(a) aluno(a): {aluno["nome"]}\nMedia do {aluno["nome"]}: {aluno["media"]}\nSituação: {aluno["situação"]}')
