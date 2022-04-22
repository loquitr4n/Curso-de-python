# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
# retornar um dicionário com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
#
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.


def notas(* n, sit=False):
    """
    -> Analisa nota de alunos.
    :param n: notas do alunos ( aceita varias notas ).
    :param sit: mostrar ou não a situação do aluno
    :return: dicionario com as notas, media, maior e menor nota do aluno.
    """
    a = dict()
    a['notas'] = n
    a['maior'] = max(n)
    a['menor'] = min(n)
    a['media'] = sum(n)/len(n)
    if sit:
        if a['media'] >= 7:
            a['situacao'] = 'BOA'
        elif 5 <= a['media'] < 7:
            a['situacao'] = 'REGULAR'
        else:
            a['situacao'] = 'RUIM'
    return a


# Programa principal:

if __name__ == '__main__':
    resp = notas(6, 7, 9, sit=True)
    print(resp)
    help(notas)
