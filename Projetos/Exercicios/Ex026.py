# Escreva um algoritmo que leia uma frase e em seguida mostre a quantidade de letras "A" existente
# na frase e  qual a posição esta a primeira e ultima letra A.

name = input('Digite uma frase: ').lower()

print('A frase tem {} letras "A"'.format(name.count('a')))
print('A primeira letra apareceu na posição {}'. format(name.find('a') + 1))
print('A ultima letra apareceu na posição {}'.format(name.rfind('a') + 1))