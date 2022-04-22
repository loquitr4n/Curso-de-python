#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

'''for c in range(1,6):
    peso = (input(f'Digite o peso da {c} pessoa: '))
print(max(peso))'''



# tirado da internet

lista = []
qtn = input('Informe a quantidade de pessoas: ')

for n in range(1,int(qtn)):
    lista.append(int(input(f'Digite o peso da {n}° pessoa: ')))

print ('O maior peso é : ', max(lista))
print ('O menor peso é : ', min(lista))






