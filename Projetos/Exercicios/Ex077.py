# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('ALEMANHA', 'BRASIL','INGLATERRA', 'DINAMARCA', 'FRANÇA', 'IRLANDA', 'JAPAO', 'INDONESIA')
for p in palavras:
    print(f'\nNa palavra {p} temos as vogais: ', end='')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')
    

