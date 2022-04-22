from Exercicios.Ex105 import notas
from Testes.manipular_arquivos import atualizar_arquivo

'''
Este programa insere um dicionario de notas de um aluno(a) no arquivo "texto.txt" 
'''
a = str(notas(5,4,2,10, sit=True))
atualizar_arquivo(f'{a}\n')



