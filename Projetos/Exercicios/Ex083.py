#Exercício Python 083: Crie um programa onde o usuário digite uma expressão
# qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está 
# com os parênteses abertos e fechados na ordem correta.

exp = input('Digite uma expreção: ')
if '(' or ')' in exp:
    a = exp.count('(')
    b = exp.count(')')
    if a == b:
        print('Sua expressão é VÁLIDA.')
    else:
        print('Sua expressão é INVÁLIDA.')
