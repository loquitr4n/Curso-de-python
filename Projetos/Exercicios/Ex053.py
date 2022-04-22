#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().replace(' ','')
print('A frase junta fica assim: {}'.format(frase))
invertida = frase[::-1].replace(' ','')
print('A frase que você digitou invertida fica: {}'.format(invertida))
if frase == invertida:
    print(f'Sendo assim, a frase \033[34m{frase}\033[m é um palindromo!')
else:
    print('Sendo assim, a frase \033[34m{}\033[m digitada não é um palindromo!'.format(frase))


